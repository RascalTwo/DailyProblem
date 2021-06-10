# Basic Regular Expression Matching

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Implement regular expression matching with the following special characters:

- `.` (period) which matches any single character
- `*` (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

## Examples

| Input                                                                                                          | Output  |
| -------------------------------------------------------------------------------------------------------------- | ------- |
| <table><tr><th>regex</th><th>string</th></tr><tr><td>`'ra.'`</td><td>`'ray'`</td></tr></table>                 | `True`  |
| <table><tr><th>regex</th><th>string</th></tr><tr><td>`'ra.'`</td><td>`'raymond'`</td></tr></table>             | `False` |
| <table><tr><th>regex</th><th>string</th></tr><tr><td>`'.*at'`</td><td>`'chat'`</td></tr></table>               | `True`  |
| <table><tr><th>regex</th><th>string</th></tr><tr><td>`'.*at'`</td><td>`'chats'`</td></tr></table>              | `False` |
| <table><tr><th>regex</th><th>string</th></tr><tr><td>`'.*'`</td><td>`'hello world'`</td></tr></table>          | `True`  |
| <table><tr><th>regex</th><th>string</th></tr><tr><td>`'abc.*'`</td><td>`'hello world'`</td></tr></table>       | `False` |
| <table><tr><th>regex</th><th>string</th></tr><tr><td>`'hel*o .*rld'`</td><td>`'hello world'`</td></tr></table> | `True`  |
