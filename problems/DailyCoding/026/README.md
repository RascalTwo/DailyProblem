# Remove Kth last node of Linked List

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a singly linked list and an integer `k`, remove the `k`th last element from the list.

> `k` is guaranteed to be smaller than the length of the list.

## Examples

| Input                                                                                                             | Output                      |
| ----------------------------------------------------------------------------------------------------------------- | --------------------------- |
| <table><tr><th>list</th><th>k</th></tr><tr><td>`Node(1, Node(2, Node(3, Node(4))))`</td><td>`0`</td></tr></table> | `Node(1, Node(2, Node(3)))` |
| <table><tr><th>list</th><th>k</th></tr><tr><td>`Node(1, Node(2, Node(3, Node(4))))`</td><td>`1`</td></tr></table> | `Node(1, Node(2, Node(4)))` |
| <table><tr><th>list</th><th>k</th></tr><tr><td>`Node(1, Node(2, Node(3, Node(4))))`</td><td>`2`</td></tr></table> | `Node(1, Node(3, Node(4)))` |
| <table><tr><th>list</th><th>k</th></tr><tr><td>`Node(1, Node(2, Node(3, Node(4))))`</td><td>`3`</td></tr></table> | `Node(2, Node(3, Node(4)))` |
