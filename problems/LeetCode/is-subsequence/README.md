# Is Subsequence

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                           | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------: | :--------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`is-subsequence`](https://leetcode.com/problems/is-subsequence) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924094/typescript_s5czgr.svg" alt="TypeScript" title="TypeScript" width="50" />](solve.ts)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given two strings `needle` and `haystack`, return `True` if `needle` is a subsequence of `haystack`, or `False` otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.

## Examples

`"ace"` is a subsequence of `"abcde"` while `"aec"` is not

| Input                                                                                                | Output  |
| ---------------------------------------------------------------------------------------------------- | ------- |
| <table><tr><th>needle</th><th>haystack</th></tr><tr><td>`"abc"`</td><td>`"ahbgdc"`</td></tr></table> | `True`  |
| <table><tr><th>needle</th><th>haystack</th></tr><tr><td>`"axc"`</td><td>`"ahbgdc"`</td></tr></table> | `False` |
