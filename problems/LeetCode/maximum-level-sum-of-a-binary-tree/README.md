# Maximum Level Sum of a Binary Tree

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                                                   | Solutions                                                                                                                                        |
| :---------------------------------------------: | :------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`maximum-level-sum-of-a-binary-tree`](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given the root of a binary tree, the level of its root is `1`, the level of its children is `2`, and so on.

Return the smallest level `x` such that the sum of all the values of nodes at level `x` is maximal.

## Examples

| Input                                                             | Output |
| ----------------------------------------------------------------- | ------ |
| `Node(1, Node(7, Node(0, Node(7, Node(-8)))))`                    | `2`    |
| `Node(989, Node(10250, Node(98693), Node(-89388, Node(-32127))))` | `2`    |
