# Remove Element

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                           | Solutions                                                                                                                                        |
| :---------------------------------------------: | :--------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`remove-element`](https://leetcode.com/problems/remove-element) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given an integer array `nums` and an integer `value`, remove all occurrences of `value` in nums in-place.

> The relative order of the elements may be changed.

If there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result.

> It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`.

## Examples

| Input                                                                                                       | Output                                    |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| <table><tr><th>nums</th><th>value</th></tr><tr><td>`[3, 2, 2, 3]`</td><td>`3`</td></tr></table>             | `2` and `nums = [2, 2, _, _]`             |
| <table><tr><th>nums</th><th>value</th></tr><tr><td>`[0, 1, 2, 2, 3, 0, 4, 2]`</td><td>`2`</td></tr></table> | `5` and `nums = [0, 1, 3, 0, 4, _, _, _]` |
