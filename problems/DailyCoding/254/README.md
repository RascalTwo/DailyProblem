# Prune Binary Tree

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Recall that a full binary tree is one in which each node is either a leaf node, or has two children.

Given a binary tree, convert it to a full one by removing nodes with only one child.

For example, given the following tree:

        0
       / \
      1   2
     /     \
    3       4
     \     / \
      5   6   7

You should convert it to:

      0
     / \
    5   4
       / \
      6   7

## Examples

| Input                                                                                | Output                                        |
| ------------------------------------------------------------------------------------ | --------------------------------------------- |
| `Node(0, Node(1, Node(3, None, Node(5))), Node(2, None, Node(4, Node(6), Node(7))))` | `Node(0, Node(5), Node(4, Node(6), Node(7)))` |
