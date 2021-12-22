# Adding Linked-List Numbers

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                             | Solutions                                                                                                                                        |
| :---------------------------------------------: | :----------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`add-two-numbers`](https://leetcode.com/problems/add-two-numbers) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Let's represent an integer in a linked list format by having each node represent a digit in the number.

Add the numbers and return the sum as a linked list.

> You may assume the numbers do not contain any leading zero, except the number `0` itself.

## Examples

| Input                                                                                                                                     | Output                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `[Node(2, Node(4, Node(3))), Node(5, Node(6, Node(4)))]`                                                                                  | `Node(7, Node(0, Node(8)))`                                              |
| `[Node(0), Node(0)]`                                                                                                                      | `Node(0)`                                                                |
| `[Node(9, Node(9)), Node(2, Node(5))]`                                                                                                    | `Node(4, Node(2, Node(1)))`                                              |
| `[Node(9, Node(9, Node(9, Node(9, Node(9, Node(9, Node(9))))))), Node(9, Node(9, Node(9, Node(9))))]`                                     | `Node(8, Node(9, Node(9, Node(9, Node(0, Node(0, Node(0, Node(1))))))))` |
| `[Node(5, Node(4, Node(3, Node(2, Node(1))))), Node(5, Node(4, Node(3, Node(2, Node(1))))), Node(5, Node(4, Node(3, Node(2, Node(1)))))]` | `Node(1, Node(6, Node(2, Node(9, Node(6, Node(3))))))`                   |
