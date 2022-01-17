# Remove Nth Node From End of List

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                                               | Solutions                                                                                                                                        |
| :---------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`remove-nth-node-from-end-of-list`](https://leetcode.com/problems/remove-nth-node-from-end-of-list) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a singly linked list and an integer `n`, remove the `n`th last element from the list.

> `n` is guaranteed to be smaller than the length of the list.

## Examples

| Input                                                                                                             | Output                      |
| ----------------------------------------------------------------------------------------------------------------- | --------------------------- |
| <table><tr><th>list</th><th>k</th></tr><tr><td>`Node(1, Node(2, Node(3, Node(4))))`</td><td>`0`</td></tr></table> | `Node(1, Node(2, Node(3)))` |
| <table><tr><th>list</th><th>k</th></tr><tr><td>`Node(1, Node(2, Node(3, Node(4))))`</td><td>`1`</td></tr></table> | `Node(1, Node(2, Node(4)))` |
| <table><tr><th>list</th><th>k</th></tr><tr><td>`Node(1, Node(2, Node(3, Node(4))))`</td><td>`2`</td></tr></table> | `Node(1, Node(3, Node(4)))` |
| <table><tr><th>list</th><th>k</th></tr><tr><td>`Node(1, Node(2, Node(3, Node(4))))`</td><td>`3`</td></tr></table> | `Node(2, Node(3, Node(4)))` |
| <table><tr><th>list</th><th>k</th></tr><tr><td>`Node(1)`</td><td>`1`</td></tr></table>                            | `None`                      |
