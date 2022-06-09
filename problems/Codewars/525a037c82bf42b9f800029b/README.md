[_metadata_:generated]: - "true"

# Partition On

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`525a037c82bf42b9f800029b`](https://www.codewars.com/kata/525a037c82bf42b9f800029b) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Write a function which partitions a list of items based on a given predicate.

After the partition function is run, the list should be of the form [ F, F, F,
T, T, T ] where the Fs (resp. Ts) are items for which the predicate function
returned false (resp. true).

NOTE: the partitioning should be **stable**; in other words: the ordering of the Fs (resp. Ts) should be preserved relative to each other.

For convenience and utility, the partition function should return the
boundary index.  In other words: the index of the first T value in items.

For example:
```coffeescript
items = [1, 2, 3, 4, 5, 6]
isEven = (n) -> n % 2 == 0
i = partitionOn isEven, items
# items should now be [1, 3, 5, 2, 4, 6]
# i     should now be 3
```
```javascript
var items = [1, 2, 3, 4, 5, 6];
function isEven(n) {return n % 2 == 0}
var i = partitionOn(isEven, items);
// items should now be [1, 3, 5, 2, 4, 6]
// i     should now be 3
```
```c
bool is_even(const void *ptr) { return *((const int *) ptr) % 2 == 0; } 
int items[] = {1, 2, 3, 4, 5, 6};
size_t i = partition_on(items, 6, sizeof(int), is_even);
// items should now be {1, 3, 5, 2, 4, 6}
// i     should now be 3
```

