# Largest Divisible Subset

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset `(i, j)` satisfies either `i % j = 0` or `j % i = 0`.

## Examples

| Input                         | Output              |
| ----------------------------- | ------------------- |
| `[3, 5, 10, 20, 21]`          | `[5, 10, 20]`       |
| `[1, 3, 6, 24]`               | `[1, 3, 6, 24]`     |
| `[1, 3, 6, 24, 12, 4, 9, 18]` | `[1, 3, 6, 24, 12]` |
