# Minimum Length of String After Deleting Similar Ends

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                                                                                       | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`minimum-length-of-string-after-deleting-similar-ends`](https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924094/typescript_s5czgr.svg" alt="TypeScript" title="TypeScript" width="50" />](solve.ts)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a string `target` consisting only of characters `a`, `b`, and `c`.

You are asked to apply the following algorithm on the string any number of times:

- Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
- Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
- The prefix and the suffix should not intersect at any index.
- The characters from the prefix and suffix must be the same.
- Delete both the prefix and the suffix.

Return the minimum length of `target` after performing the above operation any number of times (possibly zero times).

## Examples

| Input         | Output |
| ------------- | ------ |
| `'ca'`        | `0`    |
| `'cabaabac'`  | `0`    |
| `'aabccabba'` | `3`    |
| `'bab'`       | `1`    |
| `'a'`         | `1`    |
