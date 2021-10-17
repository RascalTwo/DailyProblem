# Add Binary Trees

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Write a program to merge two binary trees.

Each node in the new tree should hold a value equal to the sum of the values of the corresponding nodes of the input trees.

If only one input tree has a node in a given position, the corresponding node in the new tree should match that input node.

## Examples

| Input                                                                                                                                                    | Output                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| <table><tr><th>first</th><th>second</th></tr><tr><td>`Node(1, Node(2, Node(3), Node(4)))`</td><td>`Node(1, Node(2, Node(3), Node(4)))`</td></tr></table> | `Node(2, Node(4, Node(6), Node(8)))` |
| <table><tr><th>first</th><th>second</th></tr><tr><td>`Node(1, Node(2))`</td><td>`Node(1, None, Node(2))`</td></tr></table>                               | `Node(2, Node(2), Node(2))`          |
