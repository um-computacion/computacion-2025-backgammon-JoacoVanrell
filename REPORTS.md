# Automated Reports
## Coverage Report
```text
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
core/board.py       108      5    95%   78, 92, 118, 120, 122
core/checker.py      44      5    89%   58, 63, 65, 67, 75
core/dice.py         20      0   100%
core/game.py        131     15    89%   52, 91, 106, 137-153, 161
core/player.py       29      0   100%
-----------------------------------------------
TOTAL               332     25    92%

```
## Pylint Report
```text
************* Module core.checker
core/checker.py:80:0: C0305: Trailing newlines (trailing-newlines)
core/checker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/checker.py:3:0: C0115: Missing class docstring (missing-class-docstring)
************* Module core.game
core/game.py:55:0: C0303: Trailing whitespace (trailing-whitespace)
core/game.py:144:0: C0303: Trailing whitespace (trailing-whitespace)
core/game.py:151:0: C0303: Trailing whitespace (trailing-whitespace)
core/game.py:225:0: C0305: Trailing newlines (trailing-newlines)
core/game.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module core.board
core/board.py:197:0: C0305: Trailing newlines (trailing-newlines)
core/board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/board.py:4:0: C0115: Missing class docstring (missing-class-docstring)
core/board.py:2:0: C0411: standard import "typing.List" should be placed before local import "checker.Ficha" (wrong-import-order)
************* Module core.player
core/player.py:58:0: C0305: Trailing newlines (trailing-newlines)
core/player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/player.py:1:0: C0115: Missing class docstring (missing-class-docstring)
************* Module core.dice
core/dice.py:40:0: C0305: Trailing newlines (trailing-newlines)
core/dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/dice.py:4:0: C0115: Missing class docstring (missing-class-docstring)
************* Module cli.CLI
cli/CLI.py:29:0: C0303: Trailing whitespace (trailing-whitespace)
cli/CLI.py:72:0: C0304: Final newline missing (missing-final-newline)
cli/CLI.py:1:0: C0114: Missing module docstring (missing-module-docstring)
cli/CLI.py:1:0: C0103: Module name "CLI" doesn't conform to snake_case naming style (invalid-name)
cli/CLI.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 9.40/10


```
