# Partition Linked List

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a linked list of numbers and a pivot `k`, partition the linked list so that all nodes less than `k` come before nodes greater than or equal to `k`.

Given the linked list `5 -> 1 -> 8 -> 0 -> 3` and `k = 3`, the solution could be `1 -> 0 -> 5 -> 8 -> 3`.

## Examples

| Input                                                                                                                          | Output                                        |
| ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| <table><tr><th>list</th><th>pivot</th></tr><tr><td>`Node(5, Node(1, Node(8, Node(0, Node(3)))))`</td><td>`3`</td></tr></table> | `Node(0, Node(1, Node(5, Node(8, Node(3)))))` |
| <table><tr><th>list</th><th>pivot</th></tr><tr><td>`Node(7, Node(5, Node(3, Node(1))))`</td><td>`4`</td></tr></table>          | `Node(1, Node(3, Node(7, Node(5))))`          |
