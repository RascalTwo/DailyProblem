# Tree Symmetry

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

A tree is symmetric if its data and shape remain unchanged when it is reflected about the root node.

Given a tree, determine whether it is symmetric.

## Examples

The following tree is symmetric:

        4
       /|\
      3 5 3
     /     \
    9       9

| Input                                                            | Output  |
| ---------------------------------------------------------------- | ------- |
| `Tree(4, Tree(3, Tree(9)), Tree(5), Tree(3, Tree(9)))`           | `True`  |
| `Tree(4, Tree(3, Tree(9)), Tree(5), Tree(4, Tree(9)))`           | `False` |
| `Tree(4, Tree(3, Tree(9)), Tree(5), Tree(3, Tree(9), Tree(10)))` | `False` |
