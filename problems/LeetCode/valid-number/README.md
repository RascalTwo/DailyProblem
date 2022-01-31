# Valid Number

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                       | Solutions                                                                                                                                        |
| :---------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [LeetCode](../../../docs/providers/LeetCode.md) | [`valid-number`](https://leetcode.com/problems/valid-number) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

A valid number can be split up into these components (in order):

- A decimal number or an integer.
- (Optional) An `'e'` or `'E'`, followed by an integer.

A decimal number can be split up into these components (in order):

- (Optional) A sign character (either `'+'` or `'-'`).
- One of the following formats:
  - One or more digits, followed by a dot `'.'`.
  - One or more digits, followed by a dot `'.'`, followed by one or more digits.
  - A dot `'.'`, followed by one or more digits.

An integer can be split up into these components (in order):

- (Optional) A sign character (either `'+'` or `'-'`).
- One or more digits.

## Examples

| Input            | Output  |
| ---------------- | ------- |
| `'2'`            | `True`  |
| `'0089'`         | `True`  |
| `'-0.1'`         | `True`  |
| `'+3.14'`        | `True`  |
| `'4.'`           | `True`  |
| `'-.9'`          | `True`  |
| `'2e10'`         | `True`  |
| `'-90E3'`        | `True`  |
| `'3e+7'`         | `True`  |
| `'+6e-1'`        | `True`  |
| `'53.5e93'`      | `True`  |
| `'-123.456e789'` | `True`  |
| `'abc'`          | `False` |
| `'1a'`           | `False` |
| `'1e'`           | `False` |
| `'e3'`           | `False` |
| `'99e2.5'`       | `False` |
| `'--6'`          | `False` |
| `'-+3'`          | `False` |
| `'95a54e53'`     | `False` |
| `'6+1'`          | `False` |
| `'.-4'`          | `False` |
| `'.e1'`          | `False` |
