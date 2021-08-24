# UTF-8 Validation

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.

For example, the Euro sign, `€`, corresponds to the three bytes `11100010 10000010 10101100`.

The rules for mapping characters are as follows:

- For a single-byte character, the first bit must be zero.
- For an n-byte character, the first byte starts with n ones and a zero.
  - The other n - 1 bytes all start with 10.

Visually, this can be represented as follows.

| Bytes | Byte format                           |
| ----- | ------------------------------------- |
| `1`   | `0xxxxxxx`                            |
| `2`   | `110xxxxx 10xxxxxx`                   |
| `3`   | `1110xxxx 10xxxxxx 10xxxxxx`          |
| `4`   | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` |

Write a program that takes in an array of integers representing byte values, and returns whether it is a valid `UTF-8` encoding.

Write a method that when passes a number of integers, will return if it's a valid Unicode character representation. If the character is only one byte - only one number is passed - then the first bit must be a `0`, otherwise, for a `N`-byte character, the first byte must start with `N` `1`s and one `0`, while all the other numbers must start with `10`.

So the euro for example is - in binary - `11100010 10000010 10101100`, the first is three ones with one zero, and the other two start with `10`

## Examples

| Input                                              | Output |
| -------------------------------------------------- | ------ |
| `[0b11100010, 0b10000010, 0b10101100]`             | `'€'`  |
| `[0b01100010, 0b00000010, 0b10101100]`             | `None` |
| `[0b11110000, 0b10011111, 0b10010110, 0b10010110]` | `'🖖'` |
| `[0b01110000, 0b10101010]`                         | `None` |
| `[0b01100001]`                                     | `'a'`  |
| `[0b11100001]`                                     | `None` |
| `[0b11110000, 0b10011111, 0b10010010, 0b10101001]` | `'💩'` |
| `[0b11100000, 0b10011111, 0b10010010, 0b10101001]` | `None` |
| `[0b11000010, 0b10101110]`                         | `'®'`  |
