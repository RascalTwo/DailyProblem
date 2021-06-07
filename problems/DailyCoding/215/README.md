# Binary Tree Bottom View

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

The horizontal distance of a binary tree node describes how far left or right the node will be when the tree is printed out.

More rigorously, we can define it as follows:

- The horizontal distance of the root is `0`.
- The horizontal distance of a left child is `hd(parent) - 1`.
- The horizontal distance of a right child is `hd(parent) + 1`.

The bottom view of a tree consists of the lowest node at each horizontal distance.

If there are two nodes at the same depth and horizontal distance, either is acceptable.

Given the root to a binary tree, return its bottom view.

## Examples

For the following tree, `hd(1) = -2`, and `hd(6) = 0`.

           5
         /   \
        3     7
       / \   / \
      1   4 6   9
     /         /
    0         8

For this tree, the bottom view could be `[0, 1, 3, 6, 8, 9]`.

| Input                                                                             | Output                                        |
| --------------------------------------------------------------------------------- | --------------------------------------------- |
| `Node(5, Node(3, Node(1, Node(0)), Node(4)), Node(7, Node(6), Node(9, Node(8))))` | `[0, 1, 3, 6, 8, 9]` or `[0, 1, 3, 4, 8, 9]]` |
