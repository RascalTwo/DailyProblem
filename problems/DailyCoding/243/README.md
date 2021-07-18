# Minimize Partition Sums

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given an array of numbers `N` and an integer `k`, your task is to split `N` into `k` partitions such that the maximum sum of any partition is minimized.

## Examples

| Input                                                                                                         | Output                     |
| ------------------------------------------------------------------------------------------------------------- | -------------------------- |
| <table><tr><th>numbers</th><th>partitions</th></tr><tr><td>`[5, 1, 2, 7, 3, 4]`</td><td>`3`</td></tr></table> | `[[5, 1, 2], [7], [3, 4]]` |
| <table><tr><th>numbers</th><th>partitions</th></tr><tr><td>`[1, 2, 3]`</td><td>`3`</td></tr></table>          | `[[1], [2], [3]]`          |
| <table><tr><th>numbers</th><th>partitions</th></tr><tr><td>`[1, 2, 3]`</td><td>`2`</td></tr></table>          | `[[1, 2], [3]]`            |
