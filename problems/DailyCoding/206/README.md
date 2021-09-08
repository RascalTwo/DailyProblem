# Permutation Value

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

A permutation can be specified by an array `P`, where `P[i]` represents the location of the element at `i` in the permutation.

For example, `[2, 1, 0]` represents the permutation where elements at the index `0` and `2` are swapped.

Given an array and a permutation, apply the permutation to the array.

## Examples

Given the array `["a", "b", "c"]` and the permutation `[2, 1, 0]`, return `["c", "b", "a"]`.

| Input                                                                                                                     | Output                 |
| ------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| `input`                                                                                                                   | `output`               |
| <table><tr><th>array</th><th>permutation</th></tr><tr><td>`['a', 'b', 'c']`</td><td>`[2, 1, 0]`</td></tr></table>         | `['c', 'b', 'a']`      |
| <table><tr><th>array</th><th>permutation</th></tr><tr><td>`['d', 'a', 'c', 'b']`</td><td>`[1, 3, 2, 0]`</td></tr></table> | `['a', 'b', 'c', 'd']` |
