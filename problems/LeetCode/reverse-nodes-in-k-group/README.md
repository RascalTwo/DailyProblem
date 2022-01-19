# Reverse Nodes in k-Group

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                        |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`reverse-nodes-in-k-group`](https://leetcode.com/problems/reverse-nodes-in-k-group) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given the head of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

- `k` is a positive integer and is less than or equal to the length of the linked list.
- If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

## Examples

| Input                                                                                                                      | Output                                        |
| -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| <table><tr><th>list</th><th>k</th></tr><tr><td>`Node(1, Node(2, Node(3, Node(4, Node(5)))))`</td><td>`2`</td></tr></table> | `Node(2, Node(1, Node(4, Node(3, Node(5)))))` |
| <table><tr><th>list</th><th>k</th></tr><tr><td>`Node(1, Node(2, Node(3, Node(4, Node(5)))))`</td><td>`3`</td></tr></table> | `Node(3, Node(2, Node(1, Node(4, Node(5)))))` |
