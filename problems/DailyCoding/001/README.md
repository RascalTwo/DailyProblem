# Sum Exists

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| :---------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/java_un8ru7.svg" alt="Java" title="Java" width="50" />](solve.java) |

<!-- INFO TABLE END -->

Given a list of numbers and a number `k`, return weather any two numbers from the list add up to `k`.

## Examples

| Input                                                                                                   | Output   |
| ------------------------------------------------------------------------------------------------------- | -------- |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[10, 15, 3, 7]`</td><td>`17`</td></tr></table>     | `[0, 3]` |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[9, 4, 3, 6]`</td><td>`39`</td></tr></table>       | `None`   |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[7, 3, 15, 10]`</td><td>`17`</td></tr></table>     | `[0, 3]` |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[1, 2]`</td><td>`3`</td></tr></table>              | `[0, 1]` |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[1]`</td><td>`3`</td></tr></table>                 | `None`   |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[1, 4, 9, 6]`</td><td>`10`</td></tr></table>       | `[0, 2]` |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[1, 7, 4, 8, 6, 7]`</td><td>`12`</td></tr></table> | `[2, 3]` |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[2, 7, 11, 15]`</td><td>`9`</td></tr></table>      | `[0, 1]` |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[3, 2, 4]`</td><td>`6`</td></tr></table>           | `[1, 2]` |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[3, 3]`</td><td>`6`</td></tr></table>              | `[0, 1]` |
