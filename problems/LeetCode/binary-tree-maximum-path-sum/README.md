# Binary Tree Maximum Path Sum

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                                       | Solutions                                                                                                                                        |
| :---------------------------------------------: | :------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`binary-tree-maximum-path-sum`](https://leetcode.com/problems/binary-tree-maximum-path-sum) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a binary tree of integers, find the maximum path sum between two nodes. The path must go through at least one node, and does not need to go through the root.

## Examples

| Input                                             | Output                                              |
| ------------------------------------------------- | --------------------------------------------------- |
| `Node(1, Node(2), Node(3))`                       | `[Node(2), Node(1, Node(2), Node(3)), Node(3)]`     |
| `Node(-10, Node(9), Node(20, Node(15), Node(7)))` | `[Node(15), Node(20, Node(15), Node(17)), Node(7)]` |
