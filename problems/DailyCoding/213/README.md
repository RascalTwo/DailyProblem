# Refang IP Address

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format `A.B.C.D`, where `A`, `B`, `C`, and `D` are numbers between `0` and `255`.

> Zero-prefixed numbers, such as `01` and `065`, are not allowed, except for `0` itself.

## Examples

| Input            | Output                                                                                       |
| ---------------- | -------------------------------------------------------------------------------------------- |
| `'2542540123'`   | `[[254, 25, 40, 123], [254, 254, 0, 123]]`                                                   |
| `'128128128128'` | `[[128, 128, 128, 128]]`                                                                     |
| `'10101010'`     | `[[10, 10, 10, 10], [101, 0, 10, 10], [10, 101, 0, 10], [10, 10, 101, 0], [101, 0, 101, 0]]` |
