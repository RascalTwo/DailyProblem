# Kaprekar's constant steps

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

The number `6174` is known as `Kaprekar's constant`, after the mathematician who discovered an associated property:

> for all four-digit numbers with at least two distinct digits, repeatedly applying a simple procedure eventually results in this value.

The procedure is as follows:

> For a given input `x`, create two new numbers that consist of the digits in `x` in ascending and descending order.
>
> Subtract the smaller number from the larger number.

For example, this algorithm terminates in three steps when starting from `1234`:

    4321 - 1234 = 3087
    8730 - 0378 = 8352
    8532 - 2358 = 6174

Write a function that returns the numbers an input `N` transforms into until it becomes Kaprekar's constant

## Examples

| Input  | Output                                 |
| ------ | -------------------------------------- |
| `1234` | `[3087, 8352]`                         |
| `1495` | `[8082, 8532]`                         |
| `6451` | `[5085, 7992, 7173, 6354, 3087, 8352]` |
