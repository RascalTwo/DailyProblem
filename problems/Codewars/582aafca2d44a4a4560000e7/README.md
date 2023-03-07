[_metadata_:generated]: - "true"

# Keep the Order

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`582aafca2d44a4a4560000e7`](https://www.codewars.com/kata/582aafca2d44a4a4560000e7) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

#### Task:

Your job here is to write a function (`keepOrder` in JS/CoffeeScript, `keep_order` in Ruby/Crystal/Python, `keeporder` in Julia), which takes a sorted array `ary` and a value `val`, and returns the lowest index where you could insert `val` to maintain the sorted-ness of the array. The input array will always be sorted in ascending order. It may contain duplicates.

_Do not modify the input._

#### Some examples:

```javascript
keepOrder([1, 2, 3, 4, 7], 5) //=> 4
                      ^(index 4)
keepOrder([1, 2, 3, 4, 7], 0) //=> 0
          ^(index 0)
keepOrder([1, 1, 2, 2, 2], 2) //=> 2
                ^(index 2)
```
```coffeescript
keepOrder([1, 2, 3, 4, 7], 5) #=> 4
                      ^(index 4)
keepOrder([1, 2, 3, 4, 7], 0) #=> 0
          ^(index 0)
keepOrder([1, 1, 2, 2, 2], 2) #=> 2
                ^(index 2)
```
```ruby
keep_order([1, 2, 3, 4, 7], 5) #=> 4
                      ^(index 4)
keep_order([1, 2, 3, 4, 7], 0) #=> 0
          ^(index 0)
keep_order([1, 1, 2, 2, 2], 2) #=> 2
                ^(index 2)
```
```crystal
keep_order([1, 2, 3, 4, 7], 5) #=> 4
                      ^(index 4)
keep_order([1, 2, 3, 4, 7], 0) #=> 0
          ^(index 0)
keep_order([1, 1, 2, 2, 2], 2) #=> 2
                ^(index 2)
```
```python
keep_order([1, 2, 3, 4, 7], 5) #=> 4
                      ^(index 4)
keep_order([1, 2, 3, 4, 7], 0) #=> 0
          ^(index 0)
keep_order([1, 1, 2, 2, 2], 2) #=> 2
                ^(index 2)
```
```julia
# indexes start at 1!
keeporder([1, 2, 3, 4, 7], 5) #=> 5
                      ^(index 5)
keeporder([1, 2, 3, 4, 7], 0) #=> 1
          ^(index 1)
keeporder([1, 1, 2, 2, 2], 2) #=> 3
                ^(index 3)
```

Also check out my other creations — [Naming Files](https://www.codewars.com/kata/naming-files), [Elections: Weighted Average](https://www.codewars.com/kata/elections-weighted-average), [Identify Case](https://www.codewars.com/kata/identify-case), [Split Without Loss](https://www.codewars.com/kata/split-without-loss), [Adding Fractions](https://www.codewars.com/kata/adding-fractions),
[Random Integers](https://www.codewars.com/kata/random-integers), [Implement String#transpose](https://www.codewars.com/kata/implement-string-number-transpose), [Implement Array#transpose!](https://www.codewars.com/kata/implement-array-number-transpose), [Arrays and Procs #1](https://www.codewars.com/kata/arrays-and-procs-number-1), and [Arrays and Procs #2](https://www.codewars.com/kata/arrays-and-procs-number-2).

If you notice any issues or have any suggestions/comments whatsoever, please don't hesitate to mark an issue or just comment. Thanks!
