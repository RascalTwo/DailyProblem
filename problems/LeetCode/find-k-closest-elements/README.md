# Closest K Integers

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                             | Solutions                                                                                                                                        |
| :---------------------------------------------: | :--------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`find-k-closest-elements`](https://leetcode.com/problems/find-k-closest-elements) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a sorted integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array.

The result should also be sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:

## Examples

| Input                                                                                                                                | Output                        |
| ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- |
| <table><tr><th>array</th><th>k</th><th>x</th></tr><tr><td>`[1, 2, 3, 4, 5]`</td><td>`4`</td><td>`3`</td></tr></table>                | `[1, 2, 3, 4]`                |
| <table><tr><th>array</th><th>k</th><th>x</th></tr><tr><td>`[1, 2, 3, 4, 5]`</td><td>`4`</td><td>`-1`</td></tr></table>               | `[1, 2, 3, 4]`                |
| <table><tr><th>array</th><th>k</th><th>x</th></tr><tr><td>`[0, 1, 1, 1, 2, 3, 6, 7, 8, 9]`</td><td>`9`</td><td>`4`</td></tr></table> | `[0, 1, 1, 1, 2, 3, 6, 7, 8]` |
