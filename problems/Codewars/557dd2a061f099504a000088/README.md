[_metadata_:generated]: - "true"

# LinkedList -> Array

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`557dd2a061f099504a000088`](https://www.codewars.com/kata/557dd2a061f099504a000088) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

<b>Linked lists</b> are data structures composed of nested or chained objects, each containing a single value and a reference to the next object. 

Here's an example of a list:

```javascript
{value: 1, next: {value: 2, next: {value: 3, next: null}}}
```
```python
class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
LinkedList(1, LinkedList(2, LinkedList(3)))

```
```ruby
{value: 1, next: {value: 2, next: {value: 3, next: null}}}
```

Write a function listToArray (or list\_to\_array in Python) that converts a list to an array, like this:

```
[1, 2, 3]
```

Assume all inputs are valid lists with at least one value. For the purpose of simplicity, all values will be either numbers, strings, or Booleans.
