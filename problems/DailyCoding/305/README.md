# Remove Consecutive Nodes Summing to 0

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a linked list, remove all consecutive nodes that sum to zero.

## Examples

Suppose you are given the input `3 -> 4 -> -7 -> 5 -> -6 -> 6`.

In this case, you should first remove `3 -> 4 -> -7`, then `-6 -> 6`, leaving only `5`.

| Input                                                               | Output             |
| ------------------------------------------------------------------- | ------------------ |
| `Node(3, Node(4, Node(-7, Node(5, Node(-6, Node(6)))))))`           | `Node(5)`          |
| `Node(5, Node(3, Node(4, Node(-7, Node(5, Node(-6, Node(6))))))))`  | `Node(5, Node(5))` |
| `Node(-5, Node(3, Node(4, Node(-7, Node(5, Node(-6, Node(6))))))))` | `None`             |
