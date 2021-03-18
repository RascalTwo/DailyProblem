# Calculate Edit Distance

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other.

Given two strings, compute the edit distance between them.

## Examples

The edit distance between `“kitten”` and `“sitting”` is three: substitute the `“k”` for `“s”`, substitute the `“e”` for `“i”`, and append a `“g”`.

| Input                                                                                                     | Output |
| --------------------------------------------------------------------------------------------------------- | ------ |
| <table><tr><th>start</th><th>target</th></tr><tr><td>`'abc'`</td><td>`'bc'`</td></tr></table>             | `1`    |
| <table><tr><th>start</th><th>target</th></tr><tr><td>`'kitten'`</td><td>`'sitting'`</td></tr></table>     | `3`    |
| <table><tr><th>start</th><th>target</th></tr><tr><td>`'universe'`</td><td>`'universal'`</td></tr></table> | `2`    |
| <table><tr><th>start</th><th>target</th></tr><tr><td>`'abc'`</td><td>`'def'`</td></tr></table>            | `3`    |
| <table><tr><th>start</th><th>target</th></tr><tr><td>`''`</td><td>`'def'`</td></tr></table>               | `3`    |
| <table><tr><th>start</th><th>target</th></tr><tr><td>`'abc'`</td><td>`'cba'`</td></tr></table>            | `2`    |
| <table><tr><th>start</th><th>target</th></tr><tr><td>`'abc'`</td><td>`'abc'`</td></tr></table>            | `0`    |
