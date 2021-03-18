# Rediscover words from string

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given an array of words and a string made up of those words without any spaces, return the words of the original sentence in a list.

## Examples

| Input                                                                                                                                             | Output                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| <table><tr><th>words</th><th>string</th></tr><tr><td>`['quick', 'brown', 'the', 'fox']`</td><td>`"thequickbrownfox"`</td></tr></table>            | `['the', 'quick', 'brown', 'fox']`                                  |
| <table><tr><th>words</th><th>string</th></tr><tr><td>`['bed', 'bath', 'bedbath', 'and', 'beyond']`</td><td>`"bedbathandbeyond"`</td></tr></table> | `['bed', 'bath', 'and', 'beyond]` or `['bedbath', 'and', 'beyond']` |
