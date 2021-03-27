[_metadata_:number]:-      "158"
[_metadata_:difficulty]:-  "Medium"
[_metadata_:asker]:-       "Slack"
[_metadata_:tags]:-        "matrix"

# 158

You are given an N by M matrix of `0`s and `1`s. Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down. `0` represents an empty space while `1` represents a wall you cannot walk through.

For example, given the following matrix:

```
[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
```

Return `two`, as there are only two ways to get to the bottom right:

```
Right, down, down, right
Down, right, down, right
```

The top left corner and bottom right corner will always be `0`.
