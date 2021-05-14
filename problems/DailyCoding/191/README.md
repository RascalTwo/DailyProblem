# Remove Overlapping Intervals

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as `[0, 1]` and `[1, 2]`, but they won't be considered overlapping.

## Examples

Given the intervals `(7, 9), (2, 4), (5, 8)`, return `1` as the last interval can be removed and the first two won't overlap.

| Input                                         | Output |
| --------------------------------------------- | ------ |
| `[(0, 1), (1, 2)]`                            | `0`    |
| `[(7, 9), (2, 4), (5, 8)]`                    | `1`    |
| `[(0, 10), (2, 4), (4, 6)]`                   | `1`    |
| `[(0, 10), (2, 4), (4, 6), (6, 8), (-5, 10)]` | `2`    |
