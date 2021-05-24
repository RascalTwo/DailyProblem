# Minimum Intersecting Points

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Let `X` be a set of `n` intervals on the real line.

We say that a set of points `P` "stabs" `X` if every interval in `X` contains at least one point in `P`.

Compute the smallest set of points that stabs `X`.

## Examples

| Input                                      | Output      |
| ------------------------------------------ | ----------- |
| `[(1, 4), (4, 5), (7, 9), (9, 12)]`        | `[4, 9]`    |
| `[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]` | `[2, 3, 5]` |
