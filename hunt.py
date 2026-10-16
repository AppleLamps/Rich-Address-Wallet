#!/usr/bin/env python3
"""
Rich-Address-Wallet "hunt" scanner.

Scans every address-bearing file in this repository and reports:
  1. File inventory (files scanned, lines, candidates extracted)
  2. Address validity (format checks per coin: BTC, ETH, DOGE, DOT)
  3. Invalid / malformed entries
  4. Duplicates within each file
  5. Duplicates across files (same coin)
  6. Cross-coin overlaps (same address string listed under different coins)
  7. Richest addresses by balance (where balance data exists)

Results are written to HUNT_REPORT.md.
"""

import os
import re
import json
from collections import defaultdict, Counter

REPO = "/workspace"
OUT_REPORT = os.path.join(REPO, "HUNT_REPORT.md")
OUT_JSON = os.path.join(REPO, "HUNT_RESULTS.json")

RE_BTC_P2PKH_P2SH = re.compile(r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$")
RE_BTC_BECH32 = re.compile(r"^bc1[02-9ac-hj-np-z]{6,90}$")
RE_ETH = re.compile(r"^0x[0-9a-fA-F]{40}$")
RE_DOT = re.compile(r"^1[a-km-zA-HJ-NP-Z1-9]{40,50}$")
RE_DOGE = re.compile(r"^D[a-km-zA-HJ-NP-Z1-9]{32,34}$")


def classify(addr):
    if RE_ETH.match(addr):
        return "ETH"
    if RE_DOT.match(addr):
        return "DOT"
    if RE_BTC_P2PKH_P2SH.match(addr) or RE_BTC_BECH32.match(addr):
        return "BTC"
    if RE_DOGE.match(addr):
        return "DOGE"
    return None

FILES = [
    ("btc.txt", "BTC", "raw"),
    ("100richBTC.txt", "BTC", "raw"),
    ("Bitcoin/rich_100.txt", "BTC", "raw"),
    ("Bitcoin/rich_01.md", "BTC", "md_table"),
    ("10000BitcoinRichWalletAdd.txt", "BTC", "addr_balance"),
    ("30000BTCRichWalletAdd.txt", "BTC", "addr_balance"),
    ("6000BitcoinRichWalletAdd.txt", "BTC", "addr_balance"),
    ("Bitcoin/rich_01_Balance.txt", "BTC", "addr_balance"),
    ("798_RichWallet_BTC.txt", "BTC", "raw"),
    ("10000_RichAddressBitcoin.md", "BTC", "md_table"),
    ("Bitcoin/2023/04/RichAddr_Max-1.txt", "BTC", "raw"),
    ("Bitcoin/2023/04/RichAddr_Max-10.txt", "BTC", "raw"),
    ("Bitcoin/2023/04/P2PKH-Rich_Max-10000.md", "BTC", "md_table"),
    ("Bitcoin/2023/04/P2PKH-Rich_10000-1000.md", "BTC", "md_table"),
    ("Bitcoin/2023/04/P2PKH-Rich_1000-100.md", "BTC", "md_table"),
    ("Bitcoin/2023/04/Rich-Max_100000.md", "BTC", "md_table"),
    ("10000richAddressETH.txt", "ETH", "raw"),
    ("ETHEREUM/EthRich.txt", "ETH", "raw"),
    ("ETHEREUM/EthRich_Bal.txt", "ETH", "eth_balance"),
    ("ETHEREUM/rich_01.txt", "ETH", "raw"),
    ("ETHEREUM/rich_01.md", "ETH", "md_table"),
    ("7999_RichAddressDoge.txt", "DOGE", "doge_balance"),
    ("8K_RichAddressDoge.md", "DOGE", "md_table"),
    ("DOT/DOT-Without-Balance.txt", "DOT", "raw"),
    ("DOT/DOT-BALANCEtxt", "DOT", "dot_balance"),
]


def read_text(path):
    with open(path, "rb") as f:
        data = f.read()
    return data.decode("utf-8", errors="replace")


def extract_candidates(text, kind):
    cands = []
    if kind == "raw":
        for line in text.splitlines():
            line = line.strip()
            if line:
                cands.append(line)
    elif kind in ("addr_balance", "eth_balance", "doge_balance"):
        cands = re.findall(r"Address:\s*(\S+)", text)
    elif kind == "dot_balance":
        cands = re.findall(r"^(\S+)\s*:\s*Balance:", text, flags=re.M)
    elif kind == "md_table":
        cands = re.findall(r"`([^`]+)`", text)
    return cands


def parse_balance(text, kind):
    result = {}
    if kind == "addr_balance":
        for m in re.finditer(r"Address:\s*(\S+)\s+BALANCE:\s*([0-9.]+)\s*BTC", text):
            addr, val = m.group(1), m.group(2)
            try:
                result[addr] = max(result.get(addr, -1.0), float(val))
            except ValueError:
                pass
    elif kind == "eth_balance":
        for m in re.finditer(r"Address:\s*(\S+)\s+Balance:\s*([0-9]+)", text):
            addr, val = m.group(1), m.group(2)
            try:
                result[addr] = max(result.get(addr, -1), int(val))
            except ValueError:
                pass
    elif kind == "doge_balance":
        for m in re.finditer(r"Address:\s*(\S+)\s+-{4,}\s*BALANCE:\s*([0-9.]+)\s*DOGE", text):
            addr, val = m.group(1), m.group(2)
            try:
                result[addr] = max(result.get(addr, -1.0), float(val))
            except ValueError:
                pass
    elif kind == "dot_balance":
        for m in re.finditer(r"^(\S+)\s*:\s*Balance:([0-9.]+)", text, flags=re.M):
            addr, val = m.group(1), m.group(2)
            try:
                result[addr] = max(result.get(addr, -1.0), float(val))
            except ValueError:
                pass
    elif kind == "md_table":
        for m in re.finditer(r"\|\s*`([^`]+)`\s*\|\s*`([^`]*?)`\s*\|", text):
            addr, val = m.group(1), m.group(2)
            coin = classify(addr)
            if coin is None:
                continue
            parts = val.split()
            num = re.sub(r"[^0-9.]", "", parts[0] if parts else val)
            try:
                fval = float(num)
            except ValueError:
                continue
            result[addr] = max(result.get(addr, -1.0), fval)
    return result


def main():
    per_file = []
    coin_candidates = defaultdict(list)
    coin_invalid = defaultdict(list)
    all_invalid = []
    coin_balances = defaultdict(dict)
    addr_to_coins = defaultdict(set)

    for rel, hint, kind in FILES:
        path = os.path.join(REPO, rel)
        if not os.path.exists(path):
            per_file.append({
                "file": rel, "kind": kind, "hint": hint,
                "error": "missing", "lines": 0, "candidates": 0,
                "valid": 0, "invalid": 0, "dups_within": 0,
                "dup_addresses": [],
            })
            continue
        text = read_text(path)
        lines = text.count("\n") + (1 if text and not text.endswith("\n") else 0)
        cands = extract_candidates(text, kind)
        valid = 0
        invalid = 0
        seen_in_file = Counter()
        for c in cands:
            coin = classify(c)
            if coin is None:
                invalid += 1
                all_invalid.append((rel, c, hint))
                coin_invalid[hint].append((rel, c))
                continue
            valid += 1
            coin_candidates[coin].append((rel, c))
            seen_in_file[c] += 1
            addr_to_coins[c].add(coin)
        dups_within = sum(n - 1 for n in seen_in_file.values() if n > 1)
        dups_addrs = sorted(a for a, n in seen_in_file.items() if n > 1)
        if kind in ("addr_balance", "eth_balance", "doge_balance", "dot_balance", "md_table"):
            for addr, bal in parse_balance(text, kind).items():
                coin = classify(addr)
                if coin:
                    coin_balances[coin][addr] = max(coin_balances[coin].get(addr, -1.0), bal)
        per_file.append({
            "file": rel, "kind": kind, "hint": hint,
            "error": None, "lines": lines, "candidates": len(cands),
            "valid": valid, "invalid": invalid, "dups_within": dups_within,
            "dup_addresses": dups_addrs[:20],
        })

    cross_dups = {}
    for coin, items in coin_candidates.items():
        files_counter = defaultdict(set)
        total_counter = Counter()
        for f, a in items:
            files_counter[a].add(f)
            total_counter[a] += 1
        dups = {a: sorted(fs) for a, fs in files_counter.items() if len(fs) > 1}
        cross_dups[coin] = {
            "total_occurrences": len(items),
            "unique_addresses": len(total_counter),
            "duplicate_addresses": len(dups),
            "dup_detail": dict(sorted(dups.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:50]),
        }

    cross_coin = {}
    for addr, coins in addr_to_coins.items():
        if len(coins) > 1:
            cross_coin[addr] = sorted(coins)

    top_balances = {}
    for coin, balmap in coin_balances.items():
        top = sorted(balmap.items(), key=lambda kv: kv[1], reverse=True)[:15]
        top_balances[coin] = [(a, b) for a, b in top]

    rep = []
    rep.append("# Rich-Address-Wallet Hunt Report")
    rep.append("")
    rep.append("Automated scan of every address-bearing file in the repository. "
               "Format checks: BTC (P2PKH `1...`, P2SH `3...`, bech32 `bc1...`), "
               "ETH (`0x` + 40 hex), DOGE (`D...`), DOT/SS58 (`1...`).\n")

    rep.append("## 1. File inventory")
    rep.append("")
    rep.append("| File | Kind | Lines | Candidates | Valid | Invalid | Dups within file |")
    rep.append("|------|------|-------|------------|-------|---------|------------------|")
    tot = Counter()
    for pf in per_file:
        rep.append("| {file} | {kind} | {lines} | {candidates} | {valid} | {invalid} | {dups_within} |".format(**pf))
        tot["files"] += 1
        tot["lines"] += pf["lines"]
        tot["cands"] += pf["candidates"]
        tot["valid"] += pf["valid"]
        tot["invalid"] += pf["invalid"]
        tot["dups"] += pf["dups_within"]
    rep.append("")
    rep.append("**Totals:** {files} files scanned, {lines} lines, {cands} candidates extracted, "
               "{valid} valid addresses, {invalid} invalid entries, {dups} intra-file duplicates.\n".format(**tot))

    rep.append("## 2. Per-coin summary (unique addresses & cross-file duplicates)")
    rep.append("")
    rep.append("| Coin | Total occurrences | Unique addresses | Addresses listed in >1 file | Duplicate detail (sample) |")
    rep.append("|------|-------------------|------------------|-----------------------------|---------------------------|")
    for coin in ("BTC", "ETH", "DOGE", "DOT"):
        cd = cross_dups.get(coin, {"total_occurrences": 0, "unique_addresses": 0,
                                   "duplicate_addresses": 0, "dup_detail": {}})
        sample = ", ".join("`{}` ({} files)".format(a, len(fs))
                           for a, fs in list(cd["dup_detail"].items())[:5]) or "—"
        rep.append("| {} | {} | {} | {} | {} |".format(coin, cd["total_occurrences"],
                                                        cd["unique_addresses"],
                                                        cd["duplicate_addresses"], sample))
    rep.append("")

    rep.append("## 3. Cross-coin overlaps (same address string under multiple coins)")
    rep.append("")
    if cross_coin:
        rep.append("| Address | Coins |")
        rep.append("|---------|-------|")
        for addr, coins in sorted(cross_coin.items()):
            rep.append("| `{}` | {} |".format(addr, ", ".join(coins)))
    else:
        rep.append("None found.\n")
    rep.append("")

    rep.append("## 4. Invalid / malformed entries (format check failed)")
    rep.append("")
    if all_invalid:
        rep.append("| File | Candidate | Hinted coin |")
        rep.append("|------|-----------|-------------|")
        for f, c, hint in all_invalid[:100]:
            rep.append("| {} | `{}` | {} |".format(f, c, hint))
        if len(all_invalid) > 100:
            rep.append("| ... | ... | ... |")
        rep.append("")
        rep.append("Total invalid entries: {}.\n".format(len(all_invalid)))
    else:
        rep.append("None found.\n")

    rep.append("## 5. Richest addresses by balance (max observed across all balance files)")
    rep.append("")
    for coin in ("BTC", "ETH", "DOGE", "DOT"):
        rep.append("### {} (top 15)".format(coin))
        rep.append("")
        top = top_balances.get(coin, [])
        if top:
            rep.append("| Rank | Address | Balance |")
            rep.append("|------|---------|---------|")
            for i, (a, b) in enumerate(top, 1):
                rep.append("| {} | `{}` | {} |".format(i, a, b))
        else:
            rep.append("No balance data.\n")
        rep.append("")

    rep.append("## 6. Duplicates within individual files")
    rep.append("")
    any_dup = False
    for pf in per_file:
        if pf["dup_addresses"]:
            any_dup = True
            rep.append("### {} ({} duplicates)".format(pf["file"], pf["dups_within"]))
            rep.append("")
            for a in pf["dup_addresses"][:15]:
                rep.append("- `{}`".format(a))
            rep.append("")
    if not any_dup:
        rep.append("No intra-file duplicates.\n")

    report = "\n".join(rep)
    with open(OUT_REPORT, "w") as f:
        f.write(report)

    json_out = {
        "per_file": per_file,
        "cross_coin": cross_coin,
        "invalid": all_invalid,
        "top_balances": top_balances,
        "cross_file_duplicates": {k: v["dup_detail"] for k, v in cross_dups.items()},
        "totals": dict(tot),
    }
    with open(OUT_JSON, "w") as f:
        json.dump(json_out, f, indent=2)

    print("Hunt complete.")
    print(json.dumps(dict(tot), indent=2))
    print("Cross-coin overlaps:", len(cross_coin))
    print("Invalid entries:", len(all_invalid))
    print("Report ->", OUT_REPORT)


if __name__ == "__main__":
    main()
