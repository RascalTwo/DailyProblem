# Vote Streaming Results

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

On election day, a voting machine writes data in the form `(voter_id, candidate_id)` to a text file.

Write a program that reads this file as a stream and returns the top `3` candidates at any given time.

If you find a voter voting more than once, report this as fraud.
