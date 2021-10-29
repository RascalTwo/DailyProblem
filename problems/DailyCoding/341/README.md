# Fit Words Into Matrix

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given an `N` by `N` matrix of random letters and a dictionary of words.

Find the maximum number of words that can be packed on the board from the given dictionary.

A word is considered to be able to be packed on the board if:

- It can be found in the dictionary
- It can be constructed from untaken letters by other words found so far on the board
- The letters are adjacent to each other (vertically and horizontally, not diagonally).

Each tile can be visited only once by any word.

## Examples

Given the following dictionary:

    { 'eat', 'rain', 'in', 'rat' }

and matrix:

    [
      ['e', 'a', 'n'],
      ['t', 't', 'i'],
      ['a', 'r', 'a']
    ]

Your function should return `3`, since we can make the words `eat`, `in`, and `rat` without them touching each other.

We could have alternatively made `eat` and `rain`, but that would be incorrect since that's only `2` words.

| Input                                                                                                                                                                                                             | Output                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| <table><tr><th>words</th><th>matrix</th></tr><tr><td>`{ 'eat', 'rain', 'in', 'rat' }`</td><td>`[['e', 'a', 'n'], ['t', 't', 'i'], ['a', 'r', 'a']]`</td></tr></table>                                             | `{ 'eat', 'in', 'rat' }`        |
| <table><tr><th>words</th><th>matrix</th></tr><tr><td>`{ 'eat', 'rain', 'in', 'rat', 'pat' }`</td><td>`[['e', 'a', 'n', '0'], ['t', 't', 'i', '0'], ['a', 'r', 'a', '0'], ['p', '0', 't', '0']]`</td></tr></table> | `{ 'eat', 'in', 'rat', 'pat' }` |
