[_metadata_:generated]: - "true"

# Sum of numerous arguments

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`55c5b03f8c28da9a51000045`](https://www.codewars.com/kata/55c5b03f8c28da9a51000045) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

After calling the function `findSum()` with any number of non-negative integer arguments, it should return the sum of all those arguments.  If no arguments are given, the function should return 0, if negative arguments are given, it should return -1.

## Example

```javascript
findSum(1,2,3,4); // returns 10 
findSum(1,-2);    // returns -1 
findSum();        // returns 0 
```
```python
find_sum(1,2,3,4); # returns 10 
find_sum(1,-2);    # returns -1 
find_sum();        # returns 0 
```
```ruby
find_sum(1,2,3,4); # returns 10 
find_sum(1,-2);    # returns -1 
find_sum();        # returns 0 
```
```c
find_sum(4, 1,2,3,4); // returns 10 
find_sum(2, 1,-2);    // returns -1 
find_sum(0);          // returns  0
```

```if:javascript
**Hint:** research the arguments object on google or read Chapter 4 from Eloquent Javascript
```

```if:c
The first argument `argc` will contain the number of arguments passed to the function. The following arguments will have type `int`.
```
