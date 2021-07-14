# Phone Unlock Pattern Validator

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

One way to unlock an Android phone is through a pattern of swipes across a `1-9` keypad.

For a pattern to be valid, it must satisfy the following:

- All of its keys must be distinct.
- It must not connect two keys by jumping over a third key, unless that key has already been used.

Find the total number of valid unlock patterns of length `N`, where `1 <= N <= 9`.

## Examples

| Input | Output  |
| ----- | ------- |
| `1`   | `9`     |
| `2`   | `40`    |
| `3`   | `192`   |
| `4`   | `834`   |
| `5`   | `3280`  |
| `6`   | `11042` |
| `7`   | `29454` |
| `8`   | `55616` |
| `9`   | `55616` |
