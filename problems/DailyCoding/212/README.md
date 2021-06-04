# A1 Notation Conversion

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Spreadsheets often use this alphabetical encoding for its columns: `"A"`, `"B"`, `"C"`, ..., `"AA"`, `"AB"`, ..., `"ZZ"`, `"AAA"`, `"AAB"`, ....

Convert between this notation and numbers.

## Examples

| Input   | Output |
| ------- | ------ |
| `'A'`   | `1`    |
| `'F'`   | `6`    |
| `'Z'`   | `26`   |
| `'AA'`  | `27`   |
| `'AB'`  | `28`   |
| `'AD'`  | `30`   |
| `'AZ'`  | `52`   |
| `'BA'`  | `53`   |
| `'BZ'`  | `78`   |
| `'CA'`  | `79`   |
| `'YZ'`  | `676`  |
| `'ZA'`  | `677`  |
| `'ZZ'`  | `702`  |
| `'AAA'` | `703`  |
| `'AAB'` | `704`  |
| `'ALL'` | `1000` |

| Input  | Output  |
| ------ | ------- |
| `1`    | `'A'`   |
| `6`    | `'F'`   |
| `26`   | `'Z'`   |
| `27`   | `'AA'`  |
| `28`   | `'AB'`  |
| `30`   | `'AD'`  |
| `52`   | `'AZ'`  |
| `53`   | `'BA'`  |
| `61`   | `'BI'`  |
| `78`   | `'BZ'`  |
| `79`   | `'CA'`  |
| `676`  | `'YZ'`  |
| `677`  | `'ZA'`  |
| `702`  | `'ZZ'`  |
| `703`  | `'AAA'` |
| `704`  | `'AAB'` |
| `1000` | `'ALL'` |
