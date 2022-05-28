[_metadata_:generated]: - "true"

# Thinkful - List and Loop Drills: Lists of lists

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`586e1d458cb711f0a800033b`](https://www.codewars.com/kata/586e1d458cb711f0a800033b) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You have a two-dimensional list in the following format:

```python
data = [[2, 5], [3, 4], [8, 7]]
```

Each sub-list contains two items, and each item in the sub-lists is an integer.

Write a function `process_data()`/`processData()` that processes each sub-list like so:

 * `[2, 5]` --> `2 - 5` --> `-3`
 * `[3, 4]` --> `3 - 4` --> `-1`
 * `[8, 7]` --> `8 - 7` --> `1`
 
and then returns the product of all the processed sub-lists: `-3 * -1 * 1` --> `3`.

For input, you can trust that neither the main list nor the sublists will be empty.
