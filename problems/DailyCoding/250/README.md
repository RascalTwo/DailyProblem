# Cryptarithmetic puzzle

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

A cryptarithmetic puzzle is a mathematical game where the digits of some numbers are represented by letters.

Each letter represents a unique digit.

Given a three-word puzzle like the one above, create an algorithm that finds a solution.

## Examples

A puzzle of the form:

      SEND
    + MORE
    --------
     MONEY

may have the solution:

    {'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O', 0, 'R': 8, 'Y': 2}

| Input                                                                                                                    | Output                                                             |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `input`                                                                                                                  | `output`                                                           |
| <table><tr><th>a</th><th>b</th><th>result</th></tr><tr><td>`'send'`</td><td>`'more'`</td><td>`'money'`</td></tr></table> | `{'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O', 0, 'R': 8, 'Y': 2}` |
