[_metadata_:generated]: - "true"

# Does array x contain all values within array y?

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5143cc9694a24abcd2000001`](https://www.codewars.com/kata/5143cc9694a24abcd2000001) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

We want to extend the array class so that it provides a `contains_all?` method. This method will always assume that an array is passed in and will return `true` if all values in the passed in array are present within the current array. 

For example:

```ruby
items = [1, 2, 3, 4, 5, 6, 7, 8, 9]

items.contains_all?([1, 2, 3]) # should == true
items.contains_all?([1, 5, 13]) # should == false because 13 is not in the items array
```
```coffeescript
items = [1, 2, 3, 4, 5, 6, 7, 8, 9]

items.containsAll [1, 2, 3]  # should == true
items.containsAll [1, 5, 13] # should == false because 13 is not in the items array
```
```cpp
items = std::vector<int>{1, 2, 3, 4, 5, 6, 7, 8, 9}

contains_all(items, {1, 2, 3})  # should == true
contains_all(items, {1, 5, 13}) # should == false because 13 is not in the items array
```
```javascript
const items = [1, 2, 3, 4, 5, 6, 7, 8, 9];
items.containsAll([1, 2, 3]);  =>  true
items.containsAll([1, 5, 13]);  =>  false // because 13 is not in the items array
```
