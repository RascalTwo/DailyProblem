# Efficient String-Matching

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Implement an efficient string matching algorithm.

That is, given a string of length `N` and a pattern of length `k`, write a program that searches for the pattern in the string with less than `O(N * k)` worst-case time complexity.

If the pattern is found, return the start index of its location. If not, return `False`.

## Examples

| Input                                  | Output      |
| -------------------------------------- | ----------- |
| `'supercalifragilisticexpialidocious'` | `'super'`   |
| `'supercalifragilisticexpialidocious'` | `'docious'` |
| `'supercalifragilisticexpialidocious'` | `'fragil'`  |
| `'supercalifragilisticexpialidocious'` | `'nonezo'`  |
