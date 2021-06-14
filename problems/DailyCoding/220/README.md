# Coin Picking Game

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

In front of you is a row of `N` coins, with values `v1`, ..., `vn`.

You are asked to play the following game.

You and an opponent take turns choosing either the first or last coin from the row, removing it from the row, and receiving the value of the coin.

Write a program that returns the maximum amount of money you can win with certainty, if you move first, assuming your opponent plays optimally.

## Examples

| Input                | Output |
| -------------------- | ------ |
| `[1, 2, 3, 4, 5, 6]` | `12`   |
| `[5, 3, 1, 2, 4, 6]` | `12`   |
| `[6, 4, 2, 5, 1, 3]` | `15`   |
