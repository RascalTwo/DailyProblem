# Binary Tree Sum Range

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                               | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------: | :------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`range-sum-of-bst`](https://leetcode.com/problems/range-sum-of-bst) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924094/typescript_s5czgr.svg" alt="TypeScript" title="TypeScript" width="50" />](solve.ts)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a binary search tree and a range `[a, b]` (inclusive), return the sum of the elements of the binary search tree within the range.

## Examples

Given the following tree:

        5
       / \
      3   8
     / \ / \
    2  4 6  10

and the range `[4, 9]`, return `23` `(5 + 4 + 6 + 8)`.

| Input                                                                                                                                                 | Output |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| <table><tr><th>tree</th><th>range</th></tr><tr><td>`Node(5, Node(3, Node(2), Node(4)), Node(8, Node(6), Node(10))`</td><td>`[4, 9]`</td></tr></table> | `23`   |
| <table><tr><th>tree</th><th>range</th></tr><tr><td>`Node(5, Node(3, Node(2), Node(4)), Node(8, Node(6), Node(10))`</td><td>`[5, 5]`</td></tr></table> | `5`    |
