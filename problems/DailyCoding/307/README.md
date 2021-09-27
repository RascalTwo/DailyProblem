# Binary Search Tree Floor & Ceiling

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a binary search tree, find the floor and ceiling of a given integer.

The floor is the highest element in the tree less than or equal to an integer, while the ceiling is the lowest element in the tree greater than or equal to an integer.

If either value does not exist, return `None`.

## Examples

| Input                                                                                                                                                      | Output   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| <table><tr><th>tree</th><th>target</th></tr><tr><td>`Node(5, Node(6, Node(8), Node(7)), Node(2, Node(0), Node(3, Node(4))))`</td><td>`3`</td></tr></table> | `(2, 3)` |
| <table><tr><th>tree</th><th>target</th></tr><tr><td>`Node(5, Node(6, Node(8), Node(7)), Node(2, Node(0), Node(3, Node(4))))`</td><td>`7`</td></tr></table> | `(5, 7)` |
