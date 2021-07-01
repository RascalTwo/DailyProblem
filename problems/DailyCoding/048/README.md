# Pre & Post Traversals to Binary Tree

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

## Examples

For example, given the preorder traversal:

    [a, b, d, e, c, f, g]

or the inorder traversal:

    [d, b, e, a, f, c, g]

You should return the tree:

        a
       / \
      b   c
     / \ / \
    d  e f  g

| Input                                 | Output                                                                        |
| ------------------------------------- | ----------------------------------------------------------------------------- |
| `['a', 'b', 'd', 'e', 'c', 'f', 'g']` | `Node('a', Node('b', Node('d'), Node('e')), Node('c', Node('f'), Node('g')))` |
