# Textual Autocomplete

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Implement an autocomplete system.

That is, given a query string `s` and a set of all possible query strings, return all strings in the set that have `s` as a prefix.

## Examples

| Input                                                                                                                                                | Output                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| <table><tr><th>query</th><th>strings</th></tr><tr><td>`'de'`</td><td>`['dog', 'deer', 'deal']`</td></tr></table>                                     | `['deer', 'deal']`                         |
| <table><tr><th>query</th><th>strings</th></tr><tr><td>`'he'`</td><td>`['hello world', 'hi', 'hello', 'hell', 'head', 'universe']` </td></tr></table> | `['hell', 'hello', 'hello world', 'head']` |
