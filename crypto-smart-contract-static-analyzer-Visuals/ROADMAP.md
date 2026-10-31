# Smart contract static analyzer roadmap

Written 2026-10-30 from the repo as it stands. No dates on the
future items, because I do not know when I will be back in this
code, and a date I invent here would be a small lie in a public
file.

## Done

- Seven substring checks in analyze_contract: tx.origin,
  block.timestamp, unchecked, the three low level call forms,
  delegatecall, the weak randomness keccak256 pattern, and the
  softer msg.data plus keccak256 INFO note.
- A report file that starts fresh on each run instead of
  collecting stale results, written by log_warning and log_info
  as [WARNING] and [INFO] lines, with the same lines on the
  console.
- Honest failure paths: a missing input file prints an error
  and exits 1, and an analysis failure reports on the console
  and exits 1 instead of ending in a traceback.
- A command line with the contract path, --output, and
  --verbose, on Python 3.10 or later with no third party
  packages at all.

## Working now

- Nothing in flight. The repo holds no TODO or FIXME notes
  (I searched the tracked files on 2026-10-30) and no test
  suite; it is in a finished, working state for what it claims
  to be.

## Next

- A test suite. The repo ships none, and the checks are simple
  enough that a small set of sample contracts, one per pattern,
  would pin the current behavior down before anything grows.
- Read the note the code leaves for itself inside
  analyze_contract, which names control flow graph and pattern
  matching work as the placeholder's replacement, and decide
  how much of it this tool should honestly take on.

## Later

- More patterns, in the order I actually meet them in contract
  files, each one written as plainly as the current seven.

## Not planned

- Claiming confirmed reentrancy or overflow from a text match.
  The README says the tool cannot do that, and a pattern hit
  will stay a lead, not a verdict.
- Running or deploying the contract under scan. The file is
  read as text and nothing more.
