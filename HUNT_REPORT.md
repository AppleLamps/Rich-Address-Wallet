# Rich-Address-Wallet Hunt Report

Automated scan of every address-bearing file in the repository. Format checks: BTC (P2PKH `1...`, P2SH `3...`, bech32 `bc1...`), ETH (`0x` + 40 hex), DOGE (`D...`), DOT/SS58 (`1...`).

## 1. File inventory

| File | Kind | Lines | Candidates | Valid | Invalid | Dups within file |
|------|------|-------|------------|-------|---------|------------------|
| btc.txt | raw | 150294 | 150294 | 150294 | 0 | 0 |
| 100richBTC.txt | raw | 100 | 100 | 100 | 0 | 0 |
| Bitcoin/rich_100.txt | raw | 100 | 100 | 100 | 0 | 0 |
| Bitcoin/rich_01.md | md_table | 1028 | 1009 | 1008 | 1 | 9 |
| 10000BitcoinRichWalletAdd.txt | addr_balance | 10000 | 10000 | 10000 | 0 | 10 |
| 30000BTCRichWalletAdd.txt | addr_balance | 30000 | 29999 | 29999 | 0 | 10 |
| 6000BitcoinRichWalletAdd.txt | addr_balance | 5999 | 5999 | 5999 | 0 | 10 |
| Bitcoin/rich_01_Balance.txt | addr_balance | 10000 | 10000 | 10000 | 0 | 10 |
| 798_RichWallet_BTC.txt | raw | 798 | 798 | 798 | 0 | 1 |
| 10000_RichAddressBitcoin.md | md_table | 1028 | 1009 | 1008 | 1 | 9 |
| Bitcoin/2023/04/RichAddr_Max-1.txt | raw | 597971 | 597971 | 597956 | 15 | 0 |
| Bitcoin/2023/04/RichAddr_Max-10.txt | raw | 65031 | 65031 | 65031 | 0 | 0 |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | md_table | 64 | 116 | 56 | 60 | 0 |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | md_table | 1174 | 2337 | 1168 | 1169 | 0 |
| Bitcoin/2023/04/P2PKH-Rich_1000-100.md | md_table | 1006 | 1989 | 994 | 995 | 0 |
| Bitcoin/2023/04/Rich-Max_100000.md | md_table | 23 | 8 | 3 | 5 | 0 |
| 10000richAddressETH.txt | raw | 10000 | 10000 | 10000 | 0 | 0 |
| ETHEREUM/EthRich.txt | raw | 97307 | 97307 | 97307 | 0 | 0 |
| ETHEREUM/EthRich_Bal.txt | eth_balance | 97307 | 97307 | 97307 | 0 | 0 |
| ETHEREUM/rich_01.txt | raw | 10000 | 10000 | 10000 | 0 | 0 |
| ETHEREUM/rich_01.md | md_table | 1035 | 1022 | 1022 | 0 | 0 |
| 7999_RichAddressDoge.txt | doge_balance | 7999 | 7999 | 7751 | 248 | 0 |
| 8K_RichAddressDoge.md | md_table | 4004 | 3988 | 3779 | 209 | 0 |
| DOT/DOT-Without-Balance.txt | raw | 100 | 100 | 100 | 0 | 6 |
| DOT/DOT-BALANCEtxt | dot_balance | 100 | 100 | 100 | 0 | 6 |

**Totals:** 25 files scanned, 1102468 lines, 1104583 candidates extracted, 1101880 valid addresses, 2703 invalid entries, 71 intra-file duplicates.

## 2. Per-coin summary (unique addresses & cross-file duplicates)

| Coin | Total occurrences | Unique addresses | Addresses listed in >1 file | Duplicate detail (sample) |
|------|-------------------|------------------|-----------------------------|---------------------------|
| BTC | 874514 | 803384 | 44695 | `12ib7dApVFvg82TXKycWBNpN8kFyiAN1dr` (11 files), `12tkqA9xSoowkzoERHMWNKsTey55YEBqkv` (11 files), `17MWdxfjPYP2PYhdy885QtihfbW181r1rn` (11 files), `17rm2dvb439dZqyMe2d4D6AQJSgg6yeNRn` (11 files), `1AC4fMwgY8j9onSbXEWeH6Zan8QGMSdmtA` (11 files) |
| ETH | 215636 | 98726 | 98601 | `0x0000000000000000000000000000000000000000` (4 files), `0x000000000000000000000000000000000000dead` (4 files), `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` (4 files), `0x00000000219ab540356cbb839cbe05303d7705fa` (4 files), `0x0000006daea1723962647b7e189d311d757fb793` (4 files) |
| DOGE | 11530 | 7751 | 3779 | `D59JpTFZbTaKSW1xub9dzJmnjnbtiqbBFW` (2 files), `D59ziVykfH66REFedH2WUNc72sfJpqCUH6` (2 files), `D5A4Eb5t7RXkZD39dk6hGAKDeHr4uY4M4E` (2 files), `D5AXsyTtrH5YuQ7TxSkCov6EcGRfMNAjTE` (2 files), `D5AksXckm2tuB1NhYDsaqMYhyFtB5UzwTm` (2 files) |
| DOT | 200 | 94 | 94 | `11uxhjMSBpFKisDMg36WPVZrqELeGVteeq1eoQKhqHbXVta` (2 files), `121RoeUYcv86e3FeovWacNCS9HKYJSCqKn93UMimdncUauqz` (2 files), `123imrGvkbnUS28AVT7SSKbWA4DZYWFyQ8GSAyiFoojFRQmW` (2 files), `124BaHGGCNSZSLTsyEuEaZjpVNfDpe9SGfEk2PYwBSrFPW1t` (2 files), `12Ea3kSFDH3Meg5Br63o5BXZh4ELvhapCj96ygaXiTtpVhUM` (2 files) |

## 3. Cross-coin overlaps (same address string under multiple coins)

None found.


## 4. Invalid / malformed entries (format check failed)

| File | Candidate | Hinted coin |
|------|-----------|-------------|
| Bitcoin/rich_01.md | `
# =====================================================
# DONATE (BTC) : 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8
# Website : Mmdrza.Com
# Email : X4@mmdrza.Com
# Dev.to/Mmdrza
# Github.com/Pymmdrza
# =====================================================
` | BTC |
| 10000_RichAddressBitcoin.md | `
# =====================================================
# DONATE (BTC) : 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8
# Website : Mmdrza.Com
# Email : X4@mmdrza.Com
# Dev.to/Mmdrza
# Github.com/Pymmdrza
# =====================================================
` | BTC |
| Bitcoin/2023/04/RichAddr_Max-1.txt | `d-5d6b64787a6204d2c1b1abaefbe8f6f7` | BTC |
| Bitcoin/2023/04/RichAddr_Max-1.txt | `s-61453c839ca708f7189d9fe219c0995d` | BTC |
| Bitcoin/2023/04/RichAddr_Max-1.txt | `d-8fa7d8136e3725c52f83dd013f7d8c91` | BTC |
| Bitcoin/2023/04/RichAddr_Max-1.txt | `d-b76e26c4b905120ea59edcdcb43f842f` | BTC |
| Bitcoin/2023/04/RichAddr_Max-1.txt | `m-6d14a66d55f88b28b41132f32d1f3059` | BTC |
| Bitcoin/2023/04/RichAddr_Max-1.txt | `d-414f1537e051163a5a558d5e9ee37439` | BTC |
| Bitcoin/2023/04/RichAddr_Max-1.txt | `m-e040be9cca27d505dbe77919ccd719bd` | BTC |
| Bitcoin/2023/04/RichAddr_Max-1.txt | `d-32d7405a1734a0e222abdae0991dab48` | BTC |
| Bitcoin/2023/04/RichAddr_Max-1.txt | `d-615aedf32757e0e9640b68afc5c0df29` | BTC |
| Bitcoin/2023/04/RichAddr_Max-1.txt | `d-8ad54c49a9b665eff8c0e859d29b0e46` | BTC |
| Bitcoin/2023/04/RichAddr_Max-1.txt | `d-79d17c0ba2f202aa3389ffcbd15b0875` | BTC |
| Bitcoin/2023/04/RichAddr_Max-1.txt | `m-02787d3ed6dc0a14c9302d82a22b566a` | BTC |
| Bitcoin/2023/04/RichAddr_Max-1.txt | `m-2124c81386e37d83e6d2bad6fe6f58e4` | BTC |
| Bitcoin/2023/04/RichAddr_Max-1.txt | `d-cebf27d49b431756279e02b8ad308c69` | BTC |
| Bitcoin/2023/04/RichAddr_Max-1.txt | `s-2ad548f2459c0ed6123400e5d61a479e` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `P2PKH` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `100,000 BTC` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10,000 BTC` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `.txt` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `79957.25228327` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `53880.06271064` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `51830.39941084` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `44000.08647482` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `32321.0005131` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `31000.0722843` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `28151.05862779` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `25640.38996033` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `24495.35054524` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `23969.00183656` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `22933.58424112` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `22899.99045107` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `20479.71524275` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `20008.00224402` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `19950.00545903` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `19414.43070793` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `19371.84757979` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `17253.88054079` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `16277.00011212` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `15745.55601902` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `14040.60800188` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `14000.0007704` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `12267.02528242` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `12239.54373387` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `11533.51504708` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `11399.83296031` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `11347.47161008` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `11344.84877059` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10770.53470305` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10709.07324764` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10598.76308363` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10339.90754474` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10012.44796` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10009.26307138` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.07829836` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.03456676` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.02521437` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.01672481` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.01279339` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.01134115` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.01039895` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.01029819` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.0081734` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.00755979` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.00749219` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.0070157` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.00573704` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.00572704` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.00571704` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.00570704` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.00569704` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.00294704` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.00017114` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.00007661` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.00007114` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_Max-10000.md | `10000.0` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `.txt` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `9999.99965367` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `9872.68314284` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `9723.688719` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `9624.66362865` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `9424.7824519` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `9322.48391186` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `9260.01636283` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `9162.1210374` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `9000.0` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `8999.00610137` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `8970.80809033` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `8759.90277` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `8676.68622284` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `8575.92853558` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `8539.4967153` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `8500.20447209` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `8374.74590676` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `8176.12488626` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `8175.34526703` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `8175.34525792` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `8175.34525792` | BTC |
| Bitcoin/2023/04/P2PKH-Rich_10000-1000.md | `8175.34525792` | BTC |
| ... | ... | ... |

Total invalid entries: 2703.

## 5. Richest addresses by balance (max observed across all balance files)

### BTC (top 15)

| Rank | Address | Balance |
|------|---------|---------|
| 1 | `34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo` | 252597.2305704 |
| 2 | `bc1qgdjqv0av3q56jvd82tkdjpy7gdp9ut8tlqmgrpmv24sq90ecnvqqjwvw97` | 178010.08751098 |
| 3 | `3JJmF63ifcamPLiAmLgG96RA599yNtY3EQ` | 127351.05733404 |
| 4 | `1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ` | 121928.55523812 |
| 5 | `3LYJfcfHPXYJreMsASk2jkn69LWEYKzexb` | 116601.13655311 |
| 6 | `bc1qazcm763858nkj2dj986etajv6wquslv8uxwczt` | 94643.29914412 |
| 7 | `37XuVSEpWW4trkfmvWzegTHQt7BdktSKUs` | 94505.34101578 |
| 8 | `3M219KR5vEneNb47ewrPfWyb5jQ2DjxRP6` | 87258.00005008 |
| 9 | `38UmuUqPCrFmQo4khkomQwZ4VbY2nZMJ67` | 84067.02085008 |
| 10 | `1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF` | 79957.25228327 |
| 11 | `bc1qa5wkgaew2dkv56kfvj49j0av5nml45x9ek9hz6` | 69370.17660655 |
| 12 | `1LdRcdxfbSnmCYYNdeYpUnztiYzVfBEQeC` | 53880.06271064 |
| 13 | `1AC4fMwgY8j9onSbXEWeH6Zan8QGMSdmtA` | 51830.39941084 |
| 14 | `bc1qmxjefnuy06v345v6vhwpwt05dztztmx4g3y7wp` | 49825.72375726 |
| 15 | `3Kzh9qAqVWQhEsfQz7zEQL1EuSx5tyNLNS` | 49209.92019986 |

### ETH (top 15)

| Rank | Address | Balance |
|------|---------|---------|
| 1 | `0x00000000219ab540356cbb839cbe05303d7705fa` | 14251351007718564869804020 |
| 2 | `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` | 4116989924031555561659150 |
| 3 | `0xf977814e90da44bfa03b6295a0616a897441acec` | 2436827362084507062493640 |
| 4 | `0xda9dfa130df4de4673b89022ee50ff26f6ea73cf` | 2113030086367224616200000 |
| 5 | `0xbe0eb53f46cd790cd13851d5eff43d12404d33e8` | 1996008353439499430743490 |
| 6 | `0x742d35cc6634c0532925a3b844bc454e4438f44e` | 1542950883995291446672780 |
| 7 | `0x07ee55aa48bb72dcc6e9d78256648910de513eca` | 599196048022935468400000 |
| 8 | `0xdc24316b9ae028f1497c275eb9192a3ea0f67022` | 552504725974876018224450 |
| 9 | `0xa7efae728d2936e78bda97dc267687568dd593f3` | 527200152940594711774260 |
| 10 | `0x61edcdf5bb737adffe5043706e7c5bb1f1a56eea` | 479498953581340000000000 |
| 11 | `0xe92d1a43df510f82c66382592a047d288f85226f` | 450000050102927158850780 |
| 12 | `0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5` | 391481643312181276345820 |
| 13 | `0xcffad3200574698b78f32232aa9d63eabd290703` | 389428041490164176800160 |
| 14 | `0x1b3cb81e51011b549d78bf720b0d924ac763a7c2` | 347300004142218027746090 |
| 15 | `0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae` | 341271308210030156413190 |

### DOGE (top 15)

| Rank | Address | Balance |
|------|---------|---------|
| 1 | `DBs4WcRE7eysKwRxHNX88XZVCQ9M6QSUSz` | 30184599327.848198 |
| 2 | `DE5opaXjFgDhFBqL6tBDxTAQ56zkX6EToX` | 9752668033.041212 |
| 3 | `DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k` | 6459674782.977486 |
| 4 | `DDTtqnuZ5kfRT5qh2c7sNtqrJmV3iXYdGG` | 5031001884.83129 |
| 5 | `DH5yaieqoZN36fDVciNyRueRGvGLR3mr7L` | 4109916755.581436 |
| 6 | `DNgY1uss7Q7LkSewUXWiRhwBFk5N84aF71` | 3152645180.4522123 |
| 7 | `DGottmgfevJzhhfmvGdA2JpMjMJ1DsSKjJ` | 2381615537.9938173 |
| 8 | `DDogepartyxxxxxxxxxxxxxxxxxxw1dfzr` | 1854583718.6083906 |
| 9 | `DTXwWCTpM6pP7NtqquiMdBE385AuW1desV` | 1270009976.6500924 |
| 10 | `DQA5h47M4NdTt2mKDj4nP2VNZWczZi42RY` | 1058710375.7858061 |
| 11 | `D9a1Ah7mUNAJwNqHPER4DN9zNLoqcYFDZW` | 1000010006.0612122 |
| 12 | `D8WhgsmFUkf4imvsrwYjdhXL45LPz3bS1S` | 1000000038.7286316 |
| 13 | `D5zikmZbvK6ReZSFPDVGusqP3qKcJTjo4r` | 1000000028.421594 |
| 14 | `DEwbsuaPFeHtRKZKxUcxYqttroE4tXkMov` | 1000000027.0412122 |
| 15 | `DHPVTGcxbaqPkodQ5vj6h6uDJrkf4Sg9r2` | 1000000021.0412122 |

### DOT (top 15)

| Rank | Address | Balance |
|------|---------|---------|
| 1 | `16ZL8yLyXv3V3L3z9ofR1ovFLziyXaN1DPq4yffMAZ9czzBD` | 47420018.67637682 |
| 2 | `15j4dg5GzsL1bw2U2AWgeyAk6QTxq43V7ZPbXdAmbVLjvDCK` | 45116543.96 |
| 3 | `13UVJyLnbVp77Z2t6qa2YiTzeiZgjvXr5TzcPVvzBhtLrQQA` | 35759931.39279248 |
| 4 | `13UVJyLnbVp9RBZYFwFGyDvVd1y27Tt8tkntv6Q7JVPhFsTB` | 34694027.704587355 |
| 5 | `13UVJyLnbVp77Z2t6qZV4fNpRjDHppL6c87bHcZKG48tKJad` | 32515980.233357627 |
| 6 | `12xtAYsRUrmbniiWQqJtECiBQrMn8AypQcXhnQAc6RB6XkLW` | 26568299.200811375 |
| 7 | `1743nDTMZisPgBCYSAgkUn1kVG7MePc9rvMEjoRNf4ipVkF` | 21222652.759074964 |
| 8 | `14Ns6kKbCoka3MS4Hn6b7oRw9fFejG8RH5rq5j63cWUfpPDJ` | 20126791.443657033 |
| 9 | `14Z6CdAyMz41XNyzWh7VGj2dwNKRn1nD5PErQM1xQDvRd3Lz` | 20000003.4845 |
| 10 | `12ouvKSvKnXAdXFR5oCL1vXimWrkDWG3joMNw3ETupTRs1ab` | 16230000.0 |
| 11 | `12imiRFgMGpPPVRiXLhQixuk1jMeTrQbzSJcZ4Bj7a3idmWT` | 14493966.159686314 |
| 12 | `16DGiP6jDwAfkAeqGfkUCtheKgUzTy7UeaiFFBAv8BwX3RhN` | 12820021.418061048 |
| 13 | `11uxhjMSBpFKisDMg36WPVZrqELeGVteeq1eoQKhqHbXVta` | 12300049.944299987 |
| 14 | `12Z6FSvMFRjno881i1qpFndrtZtcVCLs5v4nR92McQNX31CT` | 12090103.876099987 |
| 15 | `14NEHDwc5PPQfEjzLVDbVbi4djQLQZ9u7mMU3BPhTFJf4cD6` | 12000001.441299988 |

## 6. Duplicates within individual files

### Bitcoin/rich_01.md (9 duplicates)

- `1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF`
- `1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ`
- `34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo`
- `37XuVSEpWW4trkfmvWzegTHQt7BdktSKUs`
- `38UmuUqPCrFmQo4khkomQwZ4VbY2nZMJ67`
- `3LYJfcfHPXYJreMsASk2jkn69LWEYKzexb`
- `3M219KR5vEneNb47ewrPfWyb5jQ2DjxRP6`
- `bc1qazcm763858nkj2dj986etajv6wquslv8uxwczt`
- `bc1qgdjqv0av3q56jvd82tkdjpy7gdp9ut8tlqmgrpmv24sq90ecnvqqjwvw97`

### 10000BitcoinRichWalletAdd.txt (10 duplicates)

- `15H8vDVWZvySPnYYTd4FmRUXnMAqykKTN3`
- `1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF`
- `1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ`
- `34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo`
- `37XuVSEpWW4trkfmvWzegTHQt7BdktSKUs`
- `38UmuUqPCrFmQo4khkomQwZ4VbY2nZMJ67`
- `3LYJfcfHPXYJreMsASk2jkn69LWEYKzexb`
- `3M219KR5vEneNb47ewrPfWyb5jQ2DjxRP6`
- `bc1qazcm763858nkj2dj986etajv6wquslv8uxwczt`
- `bc1qgdjqv0av3q56jvd82tkdjpy7gdp9ut8tlqmgrpmv24sq90ecnvqqjwvw97`

### 30000BTCRichWalletAdd.txt (10 duplicates)

- `15H8vDVWZvySPnYYTd4FmRUXnMAqykKTN3`
- `1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF`
- `1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ`
- `34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo`
- `37XuVSEpWW4trkfmvWzegTHQt7BdktSKUs`
- `38UmuUqPCrFmQo4khkomQwZ4VbY2nZMJ67`
- `3LYJfcfHPXYJreMsASk2jkn69LWEYKzexb`
- `3M219KR5vEneNb47ewrPfWyb5jQ2DjxRP6`
- `bc1qazcm763858nkj2dj986etajv6wquslv8uxwczt`
- `bc1qgdjqv0av3q56jvd82tkdjpy7gdp9ut8tlqmgrpmv24sq90ecnvqqjwvw97`

### 6000BitcoinRichWalletAdd.txt (10 duplicates)

- `15H8vDVWZvySPnYYTd4FmRUXnMAqykKTN3`
- `1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF`
- `1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ`
- `34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo`
- `37XuVSEpWW4trkfmvWzegTHQt7BdktSKUs`
- `38UmuUqPCrFmQo4khkomQwZ4VbY2nZMJ67`
- `3LYJfcfHPXYJreMsASk2jkn69LWEYKzexb`
- `3M219KR5vEneNb47ewrPfWyb5jQ2DjxRP6`
- `bc1qazcm763858nkj2dj986etajv6wquslv8uxwczt`
- `bc1qgdjqv0av3q56jvd82tkdjpy7gdp9ut8tlqmgrpmv24sq90ecnvqqjwvw97`

### Bitcoin/rich_01_Balance.txt (10 duplicates)

- `15H8vDVWZvySPnYYTd4FmRUXnMAqykKTN3`
- `1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF`
- `1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ`
- `34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo`
- `37XuVSEpWW4trkfmvWzegTHQt7BdktSKUs`
- `38UmuUqPCrFmQo4khkomQwZ4VbY2nZMJ67`
- `3LYJfcfHPXYJreMsASk2jkn69LWEYKzexb`
- `3M219KR5vEneNb47ewrPfWyb5jQ2DjxRP6`
- `bc1qazcm763858nkj2dj986etajv6wquslv8uxwczt`
- `bc1qgdjqv0av3q56jvd82tkdjpy7gdp9ut8tlqmgrpmv24sq90ecnvqqjwvw97`

### 798_RichWallet_BTC.txt (1 duplicates)

- `bc1qw8wrek2m7nlqldll66ajnwr9mh64syvkt67zlu`

### 10000_RichAddressBitcoin.md (9 duplicates)

- `1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF`
- `1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ`
- `34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo`
- `37XuVSEpWW4trkfmvWzegTHQt7BdktSKUs`
- `38UmuUqPCrFmQo4khkomQwZ4VbY2nZMJ67`
- `3LYJfcfHPXYJreMsASk2jkn69LWEYKzexb`
- `3M219KR5vEneNb47ewrPfWyb5jQ2DjxRP6`
- `bc1qazcm763858nkj2dj986etajv6wquslv8uxwczt`
- `bc1qgdjqv0av3q56jvd82tkdjpy7gdp9ut8tlqmgrpmv24sq90ecnvqqjwvw97`

### DOT/DOT-Without-Balance.txt (6 duplicates)

- `12uZhfbXmB9ZQHVhjytbvNcJFw5be8NghqtSx1JL9rfFJmt2`
- `12xtAYsRUrmbniiWQqJtECiBQrMn8AypQcXhnQAc6RB6XkLW`
- `13rRMgG1K91BQgQBGZK8ej7CBioxBnfhkkECd1WX9QpB1JvC`
- `15bNm32dQY3JKGBw5MzfaMoGEm7aVpdKas9CBuzsY8ce7sBa`
- `16SWEqB5qHed6ogWjgmEBbgs5TkR9vxVwvGRmghdGsvVnZWn`
- `1n4khJ7XCaJCTkD2isZUDsp8MjNEPLsM7YeAANCmfKD71Vy`

### DOT/DOT-BALANCEtxt (6 duplicates)

- `12uZhfbXmB9ZQHVhjytbvNcJFw5be8NghqtSx1JL9rfFJmt2`
- `12xtAYsRUrmbniiWQqJtECiBQrMn8AypQcXhnQAc6RB6XkLW`
- `13rRMgG1K91BQgQBGZK8ej7CBioxBnfhkkECd1WX9QpB1JvC`
- `15bNm32dQY3JKGBw5MzfaMoGEm7aVpdKas9CBuzsY8ce7sBa`
- `16SWEqB5qHed6ogWjgmEBbgs5TkR9vxVwvGRmghdGsvVnZWn`
- `1n4khJ7XCaJCTkD2isZUDsp8MjNEPLsM7YeAANCmfKD71Vy`
