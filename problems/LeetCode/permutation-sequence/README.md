# Permutation Sequence

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                       | Solutions                                                                                                                                        |
| :---------------------------------------------: | :--------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`permutation-sequence`](https://leetcode.com/problems/permutation-sequence) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

The set `[1, 2, 3, ..., n]` contains a total of `n`! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for `n = 3`:

> '123'
> '132'
> '213'
> '231'
> '312'
> '321'

Given `n` and `k`, return the `k`th permutation sequence.

## Examples

| Input                                                                         | Output   |
| ----------------------------------------------------------------------------- | -------- |
| <table><tr><th>n</th><th>k</th></tr><tr><td>`3`</td><td>`3`</td></tr></table> | `'213'`  |
| <table><tr><th>n</th><th>k</th></tr><tr><td>`4`</td><td>`9`</td></tr></table> | `'2314'` |
| <table><tr><th>n</th><th>k</th></tr><tr><td>`3`</td><td>`1`</td></tr></table> | `'123'`  |
