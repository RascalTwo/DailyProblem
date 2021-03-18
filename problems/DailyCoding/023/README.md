# Shortest 2D path

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given an `M` by `N` matrix consisting of booleans that represents a board.

- Each `True` boolean represents a wall.
- Each `False` boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right.

- You cannot move through walls.
- You cannot wrap around the edges of the board.

## Examples

Given the following board

    [
      [f, f, f, f],
      [t, t, f, t],
      [f, f, f, f],
      [f, f, f, f]
    ]

with a `start` of `(3, 0)` (bottom left) and `end` of `(0, 0)` (top left), the minimum number of steps required to reach the end is `7`, since we would need to go through `(1, 2)` because there is a wall everywhere else on the second row.

| Input                                                                                                                                                                                                                                        | Output |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| <table><tr><th>matrix</th><th>start</th><th>end</th></tr><tr><td>`[[False, False, False, False], [True, True, False, True], [False, False, False, False], [False, False, False, False]]`</td><td>`(3, 0)`</td><td>`(0, 0)`</td></tr></table> | `7`    |
