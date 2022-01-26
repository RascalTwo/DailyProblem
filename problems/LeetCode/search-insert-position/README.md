# Search Insert Position

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                           | Solutions                                                                                                                                        |
| :---------------------------------------------: | :------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`search-insert-position`](https://leetcode.com/problems/search-insert-position) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a sorted array of distinct integers and a target `value`, return the index if the target is found.

If not, return the index where it would be if it were inserted in order.

## Examples

| Input                                                                                            | Output |
| ------------------------------------------------------------------------------------------------ | ------ |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[1, 3, 5, 6]`</td><td>`5`</td></tr></table> | `2`    |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[1, 3, 5, 6]`</td><td>`2`</td></tr></table> | `1`    |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[1, 3, 5, 6]`</td><td>`7`</td></tr></table> | `4`    |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[1, 3, 5, 6]`</td><td>`0`</td></tr></table> | `0`    |
