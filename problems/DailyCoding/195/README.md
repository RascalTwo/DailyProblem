# Sorted Matrix Sub-Matrix Counting

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Let `A` be an `N` by `M` matrix in which every row and every column is sorted.

Given `i1`, `j1`, `i2`, and `j2`, compute the number of elements of `M` smaller than `M[i1, j1]` and larger than
`M[i2, j2]`.

## Examples

| Input                                                                                                                                                                                                                                               | Output    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| <table><tr><th>matrix</th><th>i</th><th>j</th></tr><tr><td>`[[1 , 3 , 4 , 10, 15, 20], [2 , 6 , 9 , 14, 22, 25], [3 , 8 , 10, 15, 25, 30], [10, 11, 12, 23, 30, 35], [20, 25, 30, 35, 40, 45]]`</td><td>`(1, 1)`</td><td>`(3, 3)`</td></tr></table> | `(5, 10)` |
