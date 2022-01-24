[_metadata_:slug]: - 'slug'

<!-- Optional slug, used for source text and URL, if absent populate from folder name -->

[_metadata_:url-slug]: - 'url-slug'

<!-- Optional URL-only slug, if absent populate from slug -->

[_metadata_:source]: - 'source'

<!-- Optional source URL, if absent generate from slug and provider generation method -->

# TITLE

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                                                                 | Solutions                                                                                                                                        |
| :---------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`substring-with-concatenation-of-all-words`](https://leetcode.com/problems/substring-with-concatenation-of-all-words) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given a string `s` and an array of strings words of the same length.

Return all starting indices of substring(s) in `s` that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

## Examples

| Input                                                                                                                                          | Output       |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| `input`                                                                                                                                        | `output`     |
| <table><tr><th>string</th><th>words</th></tr><tr><td>`'barfoothefoobarman'`</td><td>`["foo", "bar"]`</td></tr></table>                         | `[0, 9]`     |
| <table><tr><th>string</th><th>words</th></tr><tr><td>`'wordgoodgoodgoodbestword'`</td><td>`["word", "good", "best", "word"]`</td></tr></table> | `[]`         |
| <table><tr><th>string</th><th>words</th></tr><tr><td>`'barfoofoobarthefoobarman'`</td><td>`["bar", "foo", "the"]`</td></tr></table>            | `[6, 9, 12]` |
