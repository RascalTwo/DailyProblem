# Closest Coin

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are writing an AI for a 2D map game.

You are somewhere in a 2D grid, and there are coins strewn about over the map.

Given the position of all the coins and your current position, find the closest coin to you in terms of Manhattan distance.

That is, you can move around up, down, left, and right, but not diagonally.

If there are multiple possible closest coins, return any of them.

## Examples

Given the following map, where you are `x`, coins are `o`, and empty spaces are `.` (top left is `0, 0`):

    ---------------------
    | . | . | x | . | o |
    ---------------------
    | o | . | . | . | . |
    ---------------------
    | o | . | . | . | o |
    ---------------------
    | . | . | o | . | . |
    ---------------------

return `(0, 4)`, since that coin is closest.

| Input                                                                                                                        | Output   |
| ---------------------------------------------------------------------------------------------------------------------------- | -------- |
| <table><tr><th>position</th><th>coins</th></tr><tr><td>`(0, 2)`</td><td>`[(0, 4), (1, 0), (2, 0), (3, 2)]`</td></tr></table> | `(0, 4)` |
