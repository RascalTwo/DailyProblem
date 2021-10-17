# Elo Rating System

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

In chess, the Elo rating system is used to calculate player strengths based on game results.

A simplified description of the Elo system is as follows.

- Every player begins at the same score.
- For each subsequent game, the loser transfers some points to the winner, where the amount of points transferred depends on how unlikely the win is.
- For example, a `1200`-ranked player should gain much more points for beating a `2000`-ranked player than for beating a `1300`-ranked player.

Implement this system.
