# Island Perimeter

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                               | Solutions                                                                                                                                        |
| :---------------------------------------------: | :------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`island-perimeter`](https://leetcode.com/problems/island-perimeter) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given a 2D matrix of `1`s and `0`s where `1` represents land and `0` represents water.

Grid cells are connected horizontally orvertically (not diagonally).

The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

An island is a group is cells connected horizontally or vertically, but not diagonally. There is guaranteed to be exactly one island in this grid, and the island doesn't have water inside that isn't connected to the water around the island. Each cell has a side length of 1.

Determine the perimeter of this island.

## Examples

| Input                                                      | Output |
| ---------------------------------------------------------- | ------ |
| `[[0, 1, 1, 0], [1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 1, 0]]` | `14`   |
| `[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]` | `16`   |
| `[[1]]`                                                    | `4`    |
