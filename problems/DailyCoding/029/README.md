# Run-length encoding

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| :---------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/java_un8ru7.svg" alt="Java" title="Java" width="50" />](solve.java) |

<!-- INFO TABLE END -->

Run-length encoding is a fast and simple method of encoding strings.

The basic idea is to represent repeated successive characters as a single count and character.

Implement run-length encoding and decoding.

> You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
> You can assume the string to be decoded is valid.

## Examples

### Encode

| Input                 | Output         |
| --------------------- | -------------- |
| `''`                  | `''`           |
| `'A'`                 | `'1A'`         |
| `'AAA'`               | `'3A'`         |
| `'AAAABBBCCDAA'`      | `'4A3B2C1D2A'` |
| `'BAAAAAAAAAAAAAAAB'` | `'1B15A1B'`    |

### Decode

| Input          | Output                |
| -------------- | --------------------- |
| `''`           | `''`                  |
| `'1A'`         | `'A'`                 |
| `'3A'`         | `'AAA'`               |
| `'4A3B2C1D2A'` | `'AAAABBBCCDAA'`      |
| `'1B15A1B'`    | `'BAAAAAAAAAAAAAAAB'` |
