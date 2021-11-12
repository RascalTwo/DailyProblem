# Decode Binary Tree

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given a binary tree in a peculiar string representation.

Each node is written in the form `(lr)`, where `l` corresponds to the left child and `r` corresponds to the right child.

If either `l` or `r` is `None`, it will be represented as a `0`.

Otherwise, it will be represented by a new `(lr)` pair.

Given this representation, determine the depth of the tree.

## Examples

- A root node with no children: `(00)`
- A root node with two children: `((00)(00))`
- An unbalanced tree with three consecutive left children: `((((00)0)0)0)`

| Input           | Output                     |
| --------------- | -------------------------- |
| `input`         | `output`                   |
| `(00)`          | `Node()`                   |
| `((00)(00))`    | `Node(Node(), Node())`     |
| `((((00)0)0)0)` | `Node(Node(Node(Node())))` |
