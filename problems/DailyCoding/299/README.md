# Water Pipes Minimum-Spanning-Tree

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

A group of houses is connected to the main water plant by means of a set of pipes.

A house can either be connected by a set of pipes extending directly to the plant, or indirectly by a pipe to a nearby house which is otherwise connected.

For example, here is a possible configuration, where `A`, `B`, and `C` are houses, and arrows represent pipes:

    A <--> B <--> C <--> plant

Each pipe has an associated cost, which the utility company would like to minimize.

Given an undirected graph of pipe connections, return the lowest cost configuration of pipes such that each house has access to water.

## Examples

In the following setup, for example, we can remove all but the pipes from `plant` to `A`, `plant` to `B`, and `B` to `C`, for a total cost of 16.

    {
        'plant': {'A': 1, 'B': 5, 'C': 20},
        'A': {'C': 15},
        'B': {'C': 10},
        'C': {}
    }

| Input   | Output   |
| ------- | -------- |
| `input` | `output` |
