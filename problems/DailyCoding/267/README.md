# Is King in Check

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are presented with an `8` by `8` matrix representing the positions of pieces on a chess board.

The only pieces on the board are the black king and various white pieces.

Given this matrix, determine whether the king is in check.

## Examples

Given the following matrix:

    ...K....
    ........
    .B......
    ......P.
    .......R
    ..N.....
    ........
    .....Q..

You should return `True`, since the bishop is attacking the king diagonally.

| Input                                                                                | Output  |
| ------------------------------------------------------------------------------------ | ------- |
| `'\n...K....\n........\nB......\n......P.\n.......R\n..N.....\n........\n.....Q..'`  | `True`  |
| `'\n...K....\n........\n........\n......P.\n.......R\n..N.....\n........\n.....Q..'` | `False` |
| `'\n...K....\n...P....\n........'`                                                   | `True`  |
| `'\n...K....\n........\n...P....\n........'`                                         | `True`  |
| `'\n...K....\n........\n....N...'`                                                   | `True`  |
| `'\n...K....\n.....N..'`                                                             | `True`  |
