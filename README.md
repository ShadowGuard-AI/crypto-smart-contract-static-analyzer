![No letters and no painted board: cobbles in the near ground with a pail lid resting against a wheel and lantern light lying across both, the cart in profile in the middle ground with pails covered and tarpaulin roped, and rooftops, one lit window, and the gatehouse bell in silhouette in the far ground, with the first thinning of dark over the yard wall](intro-banner.png)

# crypto-smart-contract-static-analyzer

Title block: the first line of a fresh log page. The name above is entered in Bodoni Moda SC, chrome on coffee black, with the hour space left blank at the left and one small lantern plate beside this first heading only. The remaining headings keep the watch log form without the lantern.

![A cart lantern front on against dark: iron frame in coffee black, glass panes amber with lamplight, a chrome handle arched over the top, pink spent once as one thin reflection along the lower glass edge, and the name entered under the lantern in log hand, ruled beneath](logo.png)

![The round at its widest: a lane between yard walls an hour before dawn, the wooden cart at the left with its covered pails ranked under a tarpaulin and the carter's lantern lit on its front rail, the yard gate shut at the right with a cat asleep on its crossbar and a bell rope hanging still, and the title painted on the cart's side board in log hand, the only lettering in the scene](banner.png)

![The round in three depths: far, rooftops, the gatehouse bell, and one lit window, with the sky thinning by one shade over the life of the page; middle, the cart crossing the lane slowly from left to right at walking pace, lantern steady on its front rail, halting at the yard gate and beginning again as a new round; near, cobbles and the lantern's light pool sliding past in the opposite direction, and a cat crossing once, close, unhurried, and not crossing again](scene.svg)

![Major separator](sep-heavy.svg)

# crypto-smart-contract-static-analyzer

A small pattern matching static analyzer for smart contract source files. It reads one contract file as text and reports a short list of known risky patterns. It does not build a control flow graph, parse Solidity, or prove that a contract is safe or exploitable.

![Minor separator](sep-light.svg)

## Checks performed

- `tx.origin` usage (phishing risk)
- `block.timestamp` usage (timestamp dependence)
- The literal word `unchecked` (arithmetic that opts out of Solidity 0.8 overflow checks)
- Low level external calls: `.call{`, `.call.value(`, `.call(` (a reentrancy relevant pattern if state is updated after the call)
- `delegatecall` usage
- Weak randomness pattern `keccak256(block.difficulty, block.timestamp)`
- Informational note when `msg.data` and `keccak256` both appear

> Watch note, entered in the margin hand: A listed phrase inside a comment stops the round exactly as the same phrase in live code does, and a listed phrase inside a string literal does the same. Matching is substring matching on raw text, and a clean report means the seven strings were absent, and nothing more.

![Minor separator](sep-light.svg)

## Requirements

- Python 3.10 or later
- No third party packages. The tool uses only the Python standard library, so `requirements.txt` is intentionally empty.

![Minor separator](sep-light.svg)

## Install

```bash
git clone https://github.com/ShadowGuard-AI/crypto-smart-contract-static-analyzer.git
cd crypto-smart-contract-static-analyzer
```

![Minor separator](sep-light.svg)

## Usage

```
python3 main.py [-h] [--output OUTPUT] [--verbose] contract_code
```

- `contract_code`: path to the contract source or text file to scan (required)
- `--output OUTPUT`, `-o OUTPUT`: report file. Default: `analysis_report.txt`. The file is overwritten at the start of each run. The output path must not be the contract file itself: if the resolved output path is the same file as the input, including a relative spelling of the same path or a symlink to it, the tool prints an error and exits 1 before writing anything, so the contract source is left unchanged.
- `--verbose`, `-v`: set logging to debug level
- `-h`: show help and exit

Findings are logged to the console and appended to the report file as `[WARNING]` or `[INFO]` lines during that run.

> Watch note, entered in the margin hand: The weak randomness check is exact in argument order and spacing: the same fault written with swapped arguments or an extra space passes unseen. This check is the strictest of the seven on exactly this point.

> Watch note, entered in the margin hand: A failure partway through a round leaves the partial report standing, each line having been opened, written, and closed on its own, and that failure exits 1.

![Minor separator](sep-light.svg)

## Examples

```bash
python3 main.py contract.sol
python3 main.py contract.sol --output analysis.txt
python3 main.py contract.sol -v
```

For a contract containing `tx.origin` and `block.timestamp`, the report contains:

```
[WARNING] Potential tx.origin usage detected. This can be vulnerable to phishing attacks.
[WARNING] Potential timestamp dependence detected. This can be manipulated by miners.
[INFO] Performing basic vulnerability checks...
[INFO] Analysis completed.
```

A missing input file prints `Error: File not found: <path>` and exits with status 1.

![Minor separator](sep-light.svg)

## Limitations

- Pure substring pattern matching on the file text. It does not understand Solidity syntax, bytecode, data flow, or whether state changes happen before or after an external call, so it cannot confirm true reentrancy or integer overflow.
- A clean report only means none of the listed patterns were found.

![Minor separator](sep-light.svg)

## License

Copyright (c) ShadowGuardAI

> Watch note, entered in the margin hand: the licence line above is shown as printed and is flagged in place. It names the organisation in an unhyphenated form, while the separate LICENSE file holds the MIT License. The two stand side by side, unreconciled, as they stand in the repo.

![Minor separator](sep-light.svg)

## Diagrams and maps

I drew the tool out in [crypto-smart-contract-static-analyzer-Visuals](crypto-smart-contract-static-analyzer-Visuals/): an architecture diagram, a data-flow diagram, a flowchart of a scan, and a product map, with the written product map, statistics with citations, and the roadmap in [VISUAL.md](crypto-smart-contract-static-analyzer-Visuals/VISUAL.md). Every sheet also ships as a PNG photograph of the paper page beside its SVG.

![Smart contract analyzer architecture](crypto-smart-contract-static-analyzer-Visuals/architecture.svg)

![Major separator](sep-heavy.svg)

Log notes, entered plainly at the close. The report file is emptied at the start of each run, before findings are entered. A finished round exits 0, whether its report holds warnings or none. The story closes at the yard: the cart emptied of its round, the lantern set down still lit on the gatehouse step, the bell rope still, the cat gone from the crossbar, and the first grey over the wall arriving to find the work already done.
