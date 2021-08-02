# Binary Tree to Boustrophedon order

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth.

This style was called Boustrophedon.

Given a binary tree, write an algorithm to print the nodes in Boustrophedon order.

## Examples

Given the following tree:

           1
        /     \
      2         3
     / \       / \
    4   5     6   7

You should return `[1, 3, 2, 4, 5, 6, 7]`.

| Input                                                           | Output                  |
| --------------------------------------------------------------- | ----------------------- |
| `Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))` | `[1, 3, 2, 4, 5, 6, 7]` |
