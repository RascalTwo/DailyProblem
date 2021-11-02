# Evenly-Split Tree

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given a tree with an even number of nodes.

Consider each connection between a parent and child node to be an "edge".

You would like to remove some of these edges, such that the disconnected subtrees that remain each have an even number of nodes.

For example, suppose your input was the following tree:

       1
      / \
     2   3
        / \
       4   5
     / | \
    6  7  8

In this case, removing the edge `(3, 4)` satisfies our requirement.

Write a function that returns the maximum number of edges you can remove while still satisfying this requirement.

## Examples

| Input                                                                    | Output |
| ------------------------------------------------------------------------ | ------ |
| `Node(1, Node(2), Node(3, Node(4, Node(6), Node(7), Node(8)), Node(5)))` | `1`    |
