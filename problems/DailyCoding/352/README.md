# American Crossword Validator

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

A typical American-style crossword puzzle grid is an `N x N` matrix with black and white squares, which obeys the following rules:

- Every white square must be part of an "across" word and a "down" word.
- No word can be fewer than three letters long.
- Every white square must be reachable from every other white square.
- The grid is rotationally symmetric (for example, the colors of the top left and bottom right squares must match).

Write a program to determine whether a given matrix qualifies as a crossword grid.

## Examples

| Input                                           | Output  |
| ----------------------------------------------- | ------- |
| `['USSR_', 'META_', 'MOONS', '_UNDO', '_LEOS']` | `True`  |
| `['USSR_', 'META_', 'MOONS', '_UNDO', 'OLEOS']` | `False` |
| `['USSR_', 'META_', 'M_O_S', '_UNDO', '_LEOS']` | `False` |
| `['USSR', 'META']`                              | `False` |
