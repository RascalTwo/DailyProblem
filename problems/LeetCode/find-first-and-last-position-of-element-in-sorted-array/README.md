# Find First and Last Position of Element in Sorted Array

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                                                                                             | Solutions                                                                                                                                        |
| :---------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`find-first-and-last-position-of-element-in-sorted-array`](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return `[-1, -1]`.

## Examples

| Input                                                                                                   | Output     |
| ------------------------------------------------------------------------------------------------------- | ---------- |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[5, 7, 7, 8, 8, 10]`</td><td>`8`</td></tr></table> | `[3, 4]`   |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[5, 7, 7, 8, 8, 10]`</td><td>`6`</td></tr></table> | `[-1, -1]` |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[]`</td><td>`0`</td></tr></table>                  | `[-1, -1]` |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[]`</td><td>`0`</td></tr></table>                  | `[-1, -1]` |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[1]`</td><td>`1`</td></tr></table>                 | `[0, 0]`   |
| <table><tr><th>nums</th><th>target</th></tr><tr><td>`[2, 2]`</td><td>`2`</td></tr></table>              | `[0, 1]`   |
