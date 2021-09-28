# Determine Boolean Expression Grouping

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are presented with an array representing a `Boolean` expression. The elements are of two kinds:

`T` and `F`, representing the values `True` and `False`.
`&`, `|`, and `^`, representing the bitwise operators for `AND`, `OR`, and `XOR`.

Determine the number of ways to group the array elements using parentheses so that the entire expression evaluates to `True`.

## Examples

Suppose the input is `['F', '|', 'T', '&', 'T']`.

In this case, there are two acceptable groupings: `(F | T) & T` and `F | (T & T)`.

| Input                        | Output                                                                           |
| ---------------------------- | -------------------------------------------------------------------------------- |
| `['F', '\|', 'T', '&', 'T']` | `['(', 'F', '\|', 'T', ')', '&', 'T']` or `['F', '\|', '(', 'T', '&', 'T', ')']` |
