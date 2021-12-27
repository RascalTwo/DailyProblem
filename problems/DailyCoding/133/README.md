# Binary Search Tree Inorder Successor

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

## Examples

Here, the inorder successor of `22` is `30`.

      10
     /  \
    5   30
       /  \
      22  35

| Input                                                                                                                                | Output |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| <table><tr><th>root</th><th>number</th></tr><tr><td>`Node(10, Node(5), Node(30, Node(22), Node(35)))`</td><td>`22`</td></tr></table> | `35`   |
