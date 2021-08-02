# Ghost Probablity Calculator

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Ghost is a two-person word game where players alternate appending letters to a word.

The first person who spells out a word, or creates a prefix for which there is no possible continuation, loses.

## Examples

Here is a sample game:

    Player 1: g
    Player 2: h
    Player 1: o
    Player 2: s
    Player 1: t [loses]

Given a dictionary of words, determine the letters the first player should start with, such that with optimal play they cannot lose.

| Input                                          | Output |
| ---------------------------------------------- | ------ |
| `['cat', 'calf', 'dog', 'bear']`               | `'b'`  |
| `['cat', 'calf', 'cog', 'dog', 'bear', 'bob']` | `'b'`  |
