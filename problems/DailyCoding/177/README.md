# Rotate Linked List

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a linked list and a positive integer `k`, rotate the list to the right by `k` places.

## Examples

| Input                                                                                                                      | Output                                        |
| -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| <table><tr><th>list</th><th>k</th></tr><tr><td>`Node(7, Node(7, Node(3, Node(5))))`</td><td>`2`</td></tr></table>          | `Node(3, Node(5, Node(7, Node(7))))`          |
| <table><tr><th>list</th><th>k</th></tr><tr><td>`Node(1, Node(2, Node(3, Node(4, Node(5)))))`</td><td>`3`</td></tr></table> | `Node(3, Node(4, Node(5, Node(1, Node(2)))))` |
