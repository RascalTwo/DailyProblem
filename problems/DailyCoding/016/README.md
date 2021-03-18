# OO Circular Buffer

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You run an e-commerce website and want to record the last `N` order ids in a log.

Implement a data structure to accomplish this, with the following API:

- `record(order_id)`: adds the `order_id` to the log
- `get_last(i)`: gets the `i`th last element from the log.
  - `i` is guaranteed to be smaller than or equal to `N`.

You should be as efficient with time and space as possible.
