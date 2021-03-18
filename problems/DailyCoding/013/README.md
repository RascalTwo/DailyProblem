# Longest Substring with K distinct characters

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given an integer `k` and a string `s`, find the length of the longest substring that contains at most `k` distinct characters.

## Examples

Given `s = "abcba"` and `k = 2`, the longest substring with `k` distinct characters is `"bcb"`.

| Input                                                                                      | Output    |
| ------------------------------------------------------------------------------------------ | --------- |
| <table><tr><th>string</th><th>k</th></tr><tr><td>`"abcba"`</td><td>`2`</td></tr></table>   | `"bcb"`   |
| <table><tr><th>string</th><th>k</th></tr><tr><td>`"zabcbaz"`</td><td>`3`</td></tr></table> | `"abcba"` |
