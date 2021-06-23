# Boggle Solver

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Boggle is a game played on a `4 x 4` grid of letters.

The goal is to find as many words as possible that can be formed by a sequence of adjacent letters in the grid, using each cell at most once.

Given a game board and a dictionary of valid words, implement a Boggle solver.

## Examples

| Input                                                                                                                                                                                                                       | Output                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| <table><tr><th>board</th><th>words</th></tr><tr><td>`[['1', '2', '3', '4'], ['6', '5', '4', '5'], ['7', '2', '3', '6'], ['8', '9', '8', '7']]`</td><td>`['12', '34', '56', '78', '98', '76', '54', '32']`</td></tr></table> | `['12', '34', '56', '78', '98', '76', '54', '32']` |
| <table><tr><th>board</th><th>words</th></tr><tr><td>`[['1', '2', '3', '4'], ['2', '3', '4', '5'], ['3', '4', '5', '6'], ['4', '5', '6', '7']]`</td><td>`['1234', '567', '654', '3432']`</td></tr></table>                   | `['1234', '567', '654', '3432']`                   |
| <table><tr><th>board</th><th>words</th></tr><tr><td>`[['1', '2', '3', '4'], ['2', '3', '4', '5'], ['3', '4', '5', '6'], ['4', '5', '6', '7']]`</td><td>`['1234', '567', '654', '3432', '12', '34']`</td></tr></table>       | `['12', '34', '567', '654', '3432']`               |
