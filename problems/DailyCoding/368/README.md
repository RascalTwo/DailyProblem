# Maximum Key-Value Store

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924094/typescript_s5czgr.svg" alt="TypeScript" title="TypeScript" width="50" />](solve.ts)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Implement a key value store, where keys and values are integers, with the following methods:

- `update(key, val)`
  - Updates the value at `key` to `val`, or sets it if doesn't exist
- `get(key)`
  - Returns the value with key, or `None` if no such value exists
- `max_key(val)`
  - Returns the largest key with value `val`, or `None` if no key with that value exists
