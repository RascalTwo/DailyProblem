# Can Make Palindrome from Substring

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                                                   | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`can-make-palindrome-from-substring`](https://leetcode.com/problems/can-make-palindrome-from-substring) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924094/typescript_s5czgr.svg" alt="TypeScript" title="TypeScript" width="50" />](solve.ts) |

<!-- INFO TABLE END -->

You are given a string `haystack` and array queries where `queries[i] = [lefti, righti, ki]`.

We may rearrange the substring `haystack[lefti...righti]` for each query and then choose up to `ki` of them to replace with any lowercase English letter.

If the substring is possible to be a palindrome string after the operations above, the result of the query is `True`.

Otherwise, the result is `False`.

Return a boolean array answer where `answer[i]` is the result of the ith query `queries[i]`.

Note that each letter is counted individually for replacement, so if, for example `haystack[lefti...righti] = "aaa"`, and `ki = 2`, we can only replace two of the letters.

Also, note that no query modifies the initial string `haystack`.

## Examples

| Input                                                                                                                                                                                                                                         | Output                                                                              |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| <table><tr><th>haystack</th><th>queries</th></tr><tr><td>`'abcda'`</td><td>`[ [3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]`</td></tr></table>                                                                                       | `[True, False, False, True, True]`                                                  |
| <table><tr><th>haystack</th><th>queries</th></tr><tr><td>`'lyb'`</td><td>`[[0, 1, 0], [2, 2, 1]]`</td></tr></table>                                                                                                                           | `[False, True]`                                                                     |
| <table><tr><th>haystack</th><th>queries</th></tr><tr><td>`'rkzavgdmdgt'`</td><td>`[[5, 8, 0], [7, 9, 1], [3, 6, 4], [5, 5, 1], [8, 10, 0], [3, 9, 5], [0, 10, 10], [6, 8, 3]]`</td></tr></table>                                              | `[False, True, True, True, False, True, True, True]`                                |
| <table><tr><th>haystack</th><th>queries</th></tr><tr><td>`'hunu'`</td><td>`[[1, 1, 1], [2, 3, 0], [3, 3, 1], [0, 3, 2], [1, 3, 3], [2, 3, 1], [3, 3, 1], [0, 3, 0], [1, 1, 1], [2, 3, 0], [3, 3, 1], [0, 3, 1], [1, 1, 1]]`</td></tr></table> | `[True, False, True, True, True, True, True, False, True, False, True, True, True]` |
| <table><tr><th>haystack</th><th>queries</th></tr><tr><td>`'pqtadspgvinafefk'`</td><td>`[[1, 14, 5], [14, 15, 1], [15, 15, 1]]`</td></tr></table>                                                                                              | `[True, True, True]`                                                                |
| <table><tr><th>haystack</th><th>queries</th></tr><tr><td>`'abc'`</td><td>`[[0, 2, 0]]`</td></tr></table>                                                                                                                                      | `[False]`                                                                           |
