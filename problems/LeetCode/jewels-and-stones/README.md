# Jewels and Stones

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                 | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------: | :--------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`jewels-and-stones`](https://leetcode.com/problems/jewels-and-stones) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924094/typescript_s5czgr.svg" alt="TypeScript" title="TypeScript" width="50" />](solve.ts)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have.

You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

## Examples

| Input                                                                                              | Output |
| -------------------------------------------------------------------------------------------------- | ------ |
| <table><tr><th>jewels</th><th>stones</th></tr><tr><td>`'z'`</td><td>`'ZZ'`</td></tr></table>       | `0`    |
| <table><tr><th>jewels</th><th>stones</th></tr><tr><td>`'aA'`</td><td>`'aAAbbbb'`</td></tr></table> | `3`    |
