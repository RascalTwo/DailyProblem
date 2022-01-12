# Zigzag Conversion

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                 | Solutions                                                                                                                                        |
| :---------------------------------------------: | :--------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`zigzag-conversion`](https://leetcode.com/problems/zigzag-conversion) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this:

    P   A   H   N
    A P L S I I G
    Y   I   R

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows

## Examples

| Input                                                                                                | Output                             |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------- |
| <table><tr><th>string</th><th>rows</th></tr><tr><td>`'PAYPALISHIRING'`</td><td>`3`</td></tr></table> | `'P A H N\nA P L S I I G\nY I R'`  |
| <table><tr><th>string</th><th>rows</th></tr><tr><td>`'PAYPALISHIRING'`</td><td>`4`</td></tr></table> | `'P I N\nA L S I G\nY A H R\nP I'` |
| <table><tr><th>string</th><th>rows</th></tr><tr><td>`'A'`</td><td>`1`</td></tr></table>              | `'A'`                              |
| <table><tr><th>string</th><th>rows</th></tr><tr><td>`'AB'`</td><td>`1`</td></tr></table>             | `'AB'`                             |
