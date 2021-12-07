# Rolling Median

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given an array of numbers `arr` and a window of size `k`, return out the median of each window of size `k` starting from the left and moving right by one position each time.

Recall that the median of an even-sized list is the average of the two middle numbers.

## Examples

Given the following array and `k = 3`:

    [-1, 5, 13, 8, 2, 3, 3, 1]

Your function should return the following:

    5 <- median of [-1, 5, 13]
    8 <- median of [5, 13, 8]
    8 <- median of [13, 8, 2]
    3 <- median of [8, 2, 3]
    3 <- median of [2, 3, 3]
    3 <- median of [3, 3, 1]

| Input                        | Output               |
| ---------------------------- | -------------------- |
| `[-1, 5, 13, 8, 2, 3, 3, 1]` | `[5, 8, 8, 3, 3, 3]` |
