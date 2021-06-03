# Collatz sequence

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

if `n` is even, the next number in the sequence is `n / 2`
if `n` is odd, the next number in the sequence is `3n + 1`

It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

## Examples

| Input | Output                              |
| ----- | ----------------------------------- |
| `12`  | `[12, 6, 3, 10, 5, 16, 8, 4, 2, 1]` |
