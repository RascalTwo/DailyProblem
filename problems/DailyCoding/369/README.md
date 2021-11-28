# Price Tracking API

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924094/typescript_s5czgr.svg" alt="TypeScript" title="TypeScript" width="50" />](solve.ts)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You’re tracking stock price at a given instance of time.

Implement an API with the following functions:

- `add()`
- `update()`
- `remove()`

which adds/updates/removes a datapoint for the stock price you are tracking.

The data is given as `(timestamp, price)`, where timestamp is specified in unix epoch time.

Also, provide:

- `max()`
- `min()`
- `average()`

functions that give the max/min/average of all values seen thus far.
