# Simulate Falling Dominoes

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You are given an string representing the initial conditions of some dominoes.

Each element can take one of three values:

- `L`
  - Domino has just been pushed to the left
- `R`
  - Domino has just been pushed to the right
- `.`
  - Domino is standing still

Determine the orientation of each tile when the dominoes stop falling.

> If a domino receives a force from the left and right side simultaneously, it will remain upright.

## Examples

| Input       | Output       |
| ----------- | ------------ |
| `.L.R....L` | `LL.RRRLLL.` |
| `..R...L.L` | `..RR.LLLL.` |
