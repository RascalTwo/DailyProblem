# Tripple Sum Exists

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given an array of numbers and a number `k`, determine if there are three entries in the array which add up to the specified number `k`.

## Examples

Given `[20, 303, 3, 4, 25]` and `k = 49`, return `True` as `20 + 4 + 25 = 49`.

| Input                                                                                                                | Output                       |
| -------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[-4, 5, 2]`</td><td>`0`</td></tr></table>                       | `None`                       |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[1, 2, 3, 4]`</td><td>`9`</td></tr></table>                     | `(2, 3, 4)`                  |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[1, 5, 4, 2, 3, 6, 9, 7, 8, 10]`</td><td>`20`</td></tr></table> | `(1, 9, 10)`                 |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[-1, 0, 1, 2, -1, -4]`</td><td>`0`</td></tr></table>            | `(-1, 0, 1)` or `(1, -1, 2)` |
