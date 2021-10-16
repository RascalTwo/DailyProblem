# Construct Cartesian Tree

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

A Cartesian tree with sequence `S` is a binary tree defined by the following two properties:

It is heap-ordered, so that each parent value is strictly less than that of its children.

An in-order traversal of the tree produces nodes with values that correspond exactly to `S`.

Given a sequence `S`, construct the corresponding Cartesian tree.

## Examples

Given the sequence `[3, 2, 6, 1, 9]`, the resulting Cartesian tree would be:

          1
        /   \
      2       9
     / \
    3   6

| Input             | Output                                        |
| ----------------- | --------------------------------------------- |
| `[3, 2, 6, 1, 9]` | `Node(1, Node(2, Node(3), Node(6)), Node(9))` |
