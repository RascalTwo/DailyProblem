# Calculate Step Words

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

A step word is formed by taking a given word, adding a letter, and anagramming the result.

Given a dictionary of words and an input word, create a function that returns all valid step words.

## Examples

Starting with the word `"APPLE"`, you can add an `"A"` and anagram to get `"APPEAL"`.

| Input                                                                                                                               | Output                           |
| ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| <table><tr><th>dictionary</th><th>word</th></tr><tr><td>`['APPEAL', 'DAPPLE', 'LAPPED', 'DUMMY']`</td><td>`APPLE`</td></tr></table> | `['APPEAL', 'DAPPLE', 'LAPPED']` |
