# Quack

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

A `quack` is a data structure combining properties of both stacks and queues.

It can be viewed as a list of elements written left to right such that three operations are possible:

- `push(x)`
  - add a new item `x` to the left end of the list
- `pop()`
  - remove and return the item on the left end of the list
- `pull()`
  - remove the item on the right end of the list.

Implement a quack using three stacks and `O(1)` additional memory, so that the amortized time for any push, pop, or pull operation is `O(1)`.

## Examples

| Input   | Output   |
| ------- | -------- |
| `input` | `output` |

