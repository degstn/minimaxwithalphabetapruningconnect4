# Guidance for AI coding agents

This repository is a tiny Python Connect-Four style script. The goal of this file is to capture the minimal, actionable knowledge an AI agent needs to be productive: how the code is structured, how to run it, and important conventions and pitfalls discovered by reading the source.

Quick start
- Run the program: `python3 main.py` (this runs the sample token placements and prints two win checks and a board).
- VS Code debug: the repo contains `.vscode/launch.json` but it is a chat-replay config. To debug the Python file use the Python extension and the built-in "Python: Current File" launch configuration or add a `python` debug configuration.

Big picture / architecture
- Single-file script: `main.py` contains a `Board` class and a small integration/demo at module level. There is no package structure, no tests, and no external dependencies.
- Purpose: `Board` models a 6x7 grid (Connect Four). The module runs a deterministic sequence of moves and prints the board and win-check results when executed.

Data model & conventions (important)
- `grid` is a list of 6 rows by 7 columns: a list[list[int]] with shape 6x7. Access as `grid[y][x]`.
- Row/column orientation: `y` is the row index and `x` is the column index. Row index 0 is the bottom row; `display()` prints `grid[::-1]` so the top row shows first in output.
- Cell values: `0` = empty, `1` = red, `2` = yellow.
- Column selection API: most public methods accept `pos` as a 1-based column number (1..7). Internally this is converted to `x = pos - 1`.

API surface (what to call and what to expect)
- Class: `Board` (instantiate with `b = Board()`)
- `b.placeToken(pos)` — returns a new grid with a token placed in column `pos` for the current `b.turn` but does not mutate `b.grid` (the calling code currently does `b.updateGrid(b.placeToken(pos))`). If the column is full it prints a message and returns the current grid unchanged.
- `b.updateGrid(grid)` — assigns `b.grid = grid` and flips the turn using `b.turn = 3 - b.turn` (so 1 ↔ 2). Returns `self`.
- `b.checkWin(grid, pos)` — inspects `grid` and column `pos` for a win (vertical, horizontal, both diagonals). Returns `True/False`.
- `b.display()` — prints the board using emoji: 🔴 (red), 🟡 (yellow), 🔘 (empty).

Concrete examples from `main.py`
- Typical sequence used in the script:
  1. `b = Board()`
  2. `b.updateGrid(b.placeToken(1))` — place into column 1 and accept the returned grid
  3. `b.checkWin(b.grid, 4)` — check whether a play at column 4 produced a win

Patterns and important gotchas (do not assume standard conventions)
- The API separates token placement and state mutation: `placeToken` returns a new grid while `updateGrid` applies it and flips the turn. Many fixes or refactors will need to preserve that separation or change both callsites.
- Indexing: `pos` is 1-based. Internal indexing is 0-based: `x = pos - 1`. Remember `grid[y][x]` with y=0 as bottom row.
- Turn flip uses the compact expression `3 - self.turn` to swap 1 and 2.
- `main.py` contains demo/test code at import-time. Any automated tests or imports must account for side effects (the sample moves run on import). Consider moving demo code under `if __name__ == '__main__':` if you need import-safe behavior.

Where to start when making changes
- Small behavior change: update `main.py` functions directly and run `python3 main.py` to verify board output and printed win booleans.
- Add tests: create a new test file that imports `Board` after refactoring demo code into a `main()` function (see pattern above).
- Debugging in VS Code: add a Python debug configuration in `.vscode/launch.json` or use the Run -> Start Debugging (Python: Current File).

Files of interest
- `main.py` — primary implementation and demo harness
- `.vscode/launch.json` — contains an existing non-Python debug profile; edit or add a Python profile for step-debugging

If something is unclear
- Ask for the intended runtime behavior (should token placement mutate the object, or return updated grids?), and whether you'd like demo code extracted under `if __name__ == '__main__':` for importability. I can make a small refactor patch and add minimal tests if requested.

End of agent notes.
