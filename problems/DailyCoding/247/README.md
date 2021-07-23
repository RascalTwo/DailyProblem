# Binary Tree Height-Balanced Checker

<!-- INFO TABLE BEGIN -->

|                       Provider                        |                                                                                                                                                  Solutions                                                                                                                                                   |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Given a binary tree, determine whether or not it is height-balanced.

A height-balanced binary tree can be defined as one in which the heights of the two subtrees of any node never differ by more than one.

## Examples

| Input                                          | Output  |
| ---------------------------------------------- | ------- |
| `Node(0, Node(1, Node(2))))`                   | `False` |
| `Node(0, Node(1)))`                            | `True`  |
| `Node(0, Node(1), Node(2, Node(3))))`          | `True`  |
| `Node(0, Node(1), Node(2, Node(3, Node(4)))))` | `False` |
