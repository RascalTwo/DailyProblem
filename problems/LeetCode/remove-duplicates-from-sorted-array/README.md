# Remove Duplicates from Sorted Array

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                                                     | Solutions                                                                                                                                        |
| :---------------------------------------------: | :--------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`remove-duplicates-from-sorted-array`](https://leetcode.com/problems/remove-duplicates-from-sorted-array) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.

> The relative order of the elements should be kept the same.

If there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result.

> It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`.

## Examples

| Input                            | Output                                           |
| -------------------------------- | ------------------------------------------------ |
| `[1, 1, 2]`                      | `2` and `nums == [1, 2, _]`                      |
| `[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]` | `5` and `nums == [0, 1, 2, 3, 4, _, _, _, _, _]` |
