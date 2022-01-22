# Implement strStr()

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                               | Solutions                                                                                                                                        |
| :---------------------------------------------: | :------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`implement-strstr`](https://leetcode.com/problems/implement-strstr) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Implement `strStr()`.

Return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

## Examples

| Input                                                                                               | Output |
| --------------------------------------------------------------------------------------------------- | ------ |
| <table><tr><th>haystack</th><th>needle</th></tr><tr><td>`'hello'`</td><td>`'ll'`</td></tr></table>  | `2`    |
| <table><tr><th>haystack</th><th>needle</th></tr><tr><td>`'aaaaa'`</td><td>`'bba'`</td></tr></table> | `-1`   |
| <table><tr><th>haystack</th><th>needle</th></tr><tr><td>`''`</td><td>`''`</td></tr></table>         | `0`    |
| <table><tr><th>haystack</th><th>needle</th></tr><tr><td>`''`</td><td>`'a'`</td></tr></table>        | `-1`   |
| <table><tr><th>haystack</th><th>needle</th></tr><tr><td>`'a'`</td><td>`'a'`</td></tr></table>       | `0`    |
| <table><tr><th>haystack</th><th>needle</th></tr><tr><td>`'abc'`</td><td>`'c'`</td></tr></table>     | `2`    |
