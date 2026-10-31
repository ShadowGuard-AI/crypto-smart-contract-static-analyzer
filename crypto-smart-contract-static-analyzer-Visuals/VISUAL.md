# Smart contract static analyzer, drawn out

I made these five pictures because the README lists seven checks in
prose and the shape of the tool is easier to see than to read.
Everything in them comes from the one file that does the work,
main.py, and from the README beside it.

## The visuals

- [architecture.svg](architecture.svg): the system shape. main()
  sets up the arguments, validate_input reads the contract file as
  text, and analyze_contract runs the seven substring checks inside
  one panel, with log_warning and log_info carrying each finding to
  the console and the report file at the same time.
- [data-flow.svg](data-flow.svg): two lanes. The top lane is the
  file text moving from disk into one string in memory and through
  the substring tests. The bottom lane is where a finding goes:
  the same line printed to the console and appended to the report.
- [flowchart.svg](flowchart.svg): a run, followed as decisions.
  A file that cannot be read ends the run at exit 1. A readable
  file gets its report truncated, its seven checks in order, and
  its INFO lines, and the run exits 0 unless analyze_contract
  returned False.
- [product-map.svg](product-map.svg): the product in one frame:
  a pattern scanner in the middle, with who it serves, what goes
  in, what comes out, and where it stops at the four corners.

- [statistics.svg](statistics.svg): the numbers from the table below, drawn as bars on paper: lines by kind, with the file and commit counts noted under them.

Each sheet also ships as a PNG beside its SVG (architecture.png,
flowchart.png, and so on): the same drawing, finished as a
photograph of the paper page.

Every sheet here is drawn to look like what it is: a page sketched
by hand on paper, and each one is signed GK somewhere in the
drawing, never twice in the same place, because that is what I do
with a page I made.

## Written product map

What it is: a small pattern matching static analyzer for smart
contract source files. It reads one contract file as text and
reports a short list of known risky patterns.

Who it serves: me, reading a contract file before I trust it, and
anyone doing the same first-pass check on their own machine.

Capabilities, grouped:

- The checks, all plain substring tests on the file text:
  tx.origin usage, block.timestamp usage, the literal word
  unchecked, the low level call forms .call{, .call.value( and
  .call(, delegatecall usage, and the weak randomness pattern
  keccak256(block.difficulty, block.timestamp).
- One softer note: when msg.data and keccak256 both appear, the
  report carries an INFO line about secure keccak256 usage
  instead of a warning.
- Reporting: each finding is logged to the console and appended
  to the report file as a [WARNING] or [INFO] line. The report
  file, analysis_report.txt by default or the --output path, is
  truncated at the start of each run so old results do not pile
  up. A missing input file prints an error and exits 1, and an
  analysis failure exits 1 without a traceback.

Inputs: the path of one contract source or text file, given as
the contract_code argument. The --verbose flag only raises the
log level. Outputs: console log lines and the report file.

Boundaries, what it does NOT do: it does not parse Solidity,
build a control flow graph, or read bytecode as bytecode. It
does not know whether state changes happen before or after an
external call, so it cannot confirm true reentrancy or integer
overflow. It never runs the contract. A clean report only means
none of the listed patterns were found; it is not proof that a
contract is safe or exploitable.

## Statistics, with citations

Counted 2026-10-30, from the clone this folder ships in, at the
commit before this visuals commit (ea773334e8c7cff4030a0bf606967598b46f92eb).

| Number | Value | How it was counted, and from what |
|---|---|---|
| Files in the repo | 6 | git ls-files in the clone, counted 2026-10-30 |
| Python lines | 117 | Line count over the 1 tracked .py file (main.py), by wc -l, binary and image files excluded, 2026-10-30 |
| Markdown lines | 68 | Line count over the 1 tracked .md file (README.md), same method, 2026-10-30 |
| License lines | 21 | Line count over the tracked LICENSE file, same method, 2026-10-30 |
| requirements.txt lines | 0 | wc -l on the tracked requirements.txt, which is an empty file by design (standard library only), 2026-10-30 |
| Commits | 8 | git log in the clone, counted 2026-10-30 |
| First commit | 2025-06-18 | git log, oldest entry, 2026-10-30 |
| Last commit before this one | 2026-10-30 | git log, newest entry, 2026-10-30 |
| Tests | No test suite in the repo | No test files exist among the tracked files (git ls-files, 2026-10-30), so no tests were run and no pass is claimed |
| Smoke run | Worked, exit 0 | I ran main.py on a small sample contract holding tx.origin and block.timestamp on 2026-10-30; the report held the two expected WARNING lines plus the two INFO lines. This was a hand smoke run, not a test suite |
| Languages (API) | Python 5,213 bytes | GitHub API, GET /repos/ShadowGuard-AI/crypto-smart-contract-static-analyzer/languages, read 2026-10-30 |
| Repo size (API) | 70 KB | GitHub API, GET /repos/ShadowGuard-AI/crypto-smart-contract-static-analyzer, size field, read 2026-10-30 |
| Stars / forks (API) | 1 / 0 | Same API response, read 2026-10-30 |

External statistics: none. No outside number says anything honest
about this repo, so the repo's own numbers are the whole table.

## Roadmap summary

Done: the seven checks, the fresh report on each run, and the
exit codes that tell the truth when a file is missing or an
analysis fails. Working now: nothing in flight. Next, if I return
to it: the harder analysis the code itself names in a comment,
control flow and real pattern work past substring matching. The
full roadmap, with the Later and Not planned sections, is in
[ROADMAP.md](ROADMAP.md).
