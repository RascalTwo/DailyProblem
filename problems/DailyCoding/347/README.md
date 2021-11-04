# Minimal Queue-String

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given a string of length `N` and a parameter `k`.

The string can be manipulated by taking one of the first `k` letters and moving it to the end.

Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.

For example, suppose we are given the string `daily` and `k = 1`. The best we can create in this case is `ailyd`.

## Examples

| Input                                                                                    | Output    |
| ---------------------------------------------------------------------------------------- | --------- |
| <table><tr><th>string</th><th>k</th></tr><tr><td>`'daily'`</td><td>`1`</td></tr></table> | `'ailyd'` |
| <table><tr><th>string</th><th>k</th></tr><tr><td>`'daily'`</td><td>`2`</td></tr></table> | `'ailyd'` |
| <table><tr><th>string</th><th>k</th></tr><tr><td>`'daily'`</td><td>`3`</td></tr></table> | `'ailyd'` |
| <table><tr><th>string</th><th>k</th></tr><tr><td>`'daily'`</td><td>`4`</td></tr></table> | `'ailyd'` |
| <table><tr><th>string</th><th>k</th></tr><tr><td>`'daily'`</td><td>`5`</td></tr></table> | `'adily'` |
