[_metadata_:number]:-      "230"
[_metadata_:difficulty]:-  "Medium"
[_metadata_:asker]:-       "Sachs"
[_metadata_:tags]:-        "math"

# 230

You are given `N` identical eggs and access to a building with `k` floors.

Your task is to find the lowest floor that will cause an egg to break, if dropped from that floor.

Once an egg breaks, it cannot be dropped again.

If an egg breaks when dropped from the `x`th floor, you can assume it will also break when dropped from any floor greater than `x`.

Write an algorithm that finds the minimum number of trial drops it will take, in the worst case, to identify this floor.

For example, if `N = 1` and `k = 5`, we will need to try dropping the egg at every floor, beginning with the first, until we reach the fifth floor, so our solution will be `5`.