# Toeplitz Matrix

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

A `Toeplitz` matrix is one in which the elements on any given diagonal from top left to bottom right are identical.

Determine whether a given input is a `Toeplitz` matrix.

## Examples

    1 2 3 4 8
    5 1 2 3 4
    4 5 1 2 3
    7 4 5 1 2

| Input                                                                    | Output  |
| ------------------------------------------------------------------------ | ------- |
| `[ [1, 2, 3, 4, 8], [5, 1, 2, 3, 4], [4, 5, 1, 2, 3], [7, 4, 5, 1, 2] ]` | `True`  |
| `[ [0, 2, 3, 4, 8], [5, 1, 2, 3, 4], [4, 5, 1, 2, 3], [7, 4, 5, 1, 2] ]` | `False` |
| `[ [1, 2, 3, 0, 8], [5, 1, 2, 3, 4], [4, 5, 1, 2, 3], [7, 4, 5, 1, 2] ]` | `False` |
| `[ [1, 2, 3, 0, 8], [5, 1, 2, 3, 4], [4, 5, 1, 2, 3], [7, 0, 5, 1, 2] ]` | `False` |
