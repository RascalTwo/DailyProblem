# Embolden String

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Implement the function `embolden(s, lst)` which takes in a string `s` and list of substrings `lst`, and wraps all substrings in `s` with an HTML bold tag `<b>` and `</b>`.

If two bold tags overlap or are contiguous, they should be merged.

## Examples

| Input                                                                                                          | Output                  |
| -------------------------------------------------------------------------------------------------------------- | ----------------------- |
| <table><tr><th>string</th><th>substrings</th></tr><tr><td>`abcdefg`</td><td>`["bc", "ef"]`</td></tr></table>   | `a<b>bc</b>d<b>ef</b>g` |
| <table><tr><th>string</th><th>substrings</th></tr><tr><td>`abcdefg`</td><td>`["bcd", "def"]`</td></tr></table> | `a<b>bcdef</b>g`        |
