# Find Rectangle in Matrix

<!-- INFO TABLE BEGIN -->

| Provider                                          | Solutions                                                                                                                                        |
| :-----------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [Arbitrary](../../../docs/providers/Arbitrary.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a matrix of 0's and 1's, return if there are any four corners of 1's that form a rectangle.

## Examples

| Input                                                                                   | Output  |
| --------------------------------------------------------------------------------------- | ------- |
| `[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]` | `False` |
| `[[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]` | `True`  |
| `[[1, 0, 1, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]` | `False` |
| `[[1, 1, 1, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 0]]` | `True`  |
