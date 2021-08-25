# Group Friends

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

A classroom consists of `N` students, whose friendships can be represented in an adjacency list.

Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations.

In other words, this is the smallest set such that no student in the group has any friends outside this group.

Given a friendship list such as the one above, determine the number of friend groups in the class.

## Examples

For example, the following describes a situation where `0` is friends with `1` and `2`, `3` is friends with `6`, and so on.

    {
      0: [1, 2],
      1: [0, 5],
      2: [0],
      3: [6],
      4: [],
      5: [1],
      6: [3]
    }

For the example above, the friend groups would be `{0, 1, 2, 5}`, `{3, 6}`, `{4}`.

| Input                                                                                                                                          | Output                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `{0: [1, 2], 1: [0, 5], 2: [0], 3: [6], 4: [], 5: [1], 6: [3]}`                                                                                | `[{0, 1, 2, 5}, {3, 6}, {4}]`                                          |
| `{'Jack': ['Henry', 'Bob'], 'Henry': ['Jack', 'Mike'], 'Bob': ['Jack'], 'Sally': ['Lindsey'], 'Ashley': [], 'Mike': ['Henry'], 'Lindsey': []}` | `[{'Jack', 'Henry', 'Bob', 'Mike'}, {'Sally', 'Lindsey'}, {'Ashley'}]` |
