[_metadata_:generated]: - "true"

# Making Copies

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`53d2697b7152a5e13d000b82`](https://www.codewars.com/kata/53d2697b7152a5e13d000b82) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Write a function that takes a list (in Python) or array (in other languages) of numbers, and makes a copy of it.

Note that you may have troubles if you do not return an actual copy, item by item, just a pointer or an alias for an existing list or array.

If not a list or array is given as a parameter in interpreted languages, the function should raise an error.

Examples:
```python
t = [1, 2, 3, 4]
t_copy = copy_list(t)

t[1] += 5
t = [1, 7, 3, 4]
t_copy = [1, 2, 3, 4]
```
```javascript
t = [1, 2, 3, 4]
tCopy = copyList(t)
t[1] += 5
t = [1, 7, 3, 4]
tCopy = [1, 2, 3, 4]
```
```csharp
List<int> lst = new int[] {1, 2, 3, 4}.ToList();
List<int> lstCopy = lst.Copy();
lst[1] += 5;
lst == {1, 7, 3, 4};
lstCopy == {1, 2, 3, 4};
```
