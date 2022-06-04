[_metadata_:generated]: - "true"

# Custom Array Filters

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`53fc954904a45eda6b00097f`](https://www.codewars.com/kata/53fc954904a45eda6b00097f) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Dave has a lot of data he is required to apply filters to, which are simple enough, but he wants a shorter way of doing so.

He wants the following functions to work as expected:
```ruby
even # [1,2,3,4,5].even should return [2,4]
odd # [1,2,3,4,5].odd should return [1,3,5]
under # [1,2,3,4,5].under(4) should return [1,2,3]
over # [1,2,3,4,5].over(4) should return [5]
in_range # [1,2,3,4,5].in_range(1..3) should return [1,2,3]
```
```javascript
even    // [1,2,3,4,5].even() should return [2,4]
odd     // [1,2,3,4,5].odd() should return [1,3,5]
under   // [1,2,3,4,5].under(4) should return [1,2,3]
over    // [1,2,3,4,5].over(4) should return [5]
inRange // [1,2,3,4,5].inRange(1,3) should return [1,2,3]
```
```python
even # list([1,2,3,4,5]).even() should return [2,4]
odd # list([1,2,3,4,5]).odd() should return [1,3,5]
under # list([1,2,3,4,5]).under(4) should return [1,2,3]
over # list([1,2,3,4,5]).over(4) should return [5]
in_range # list([1,2,3,4,5]).in_range(1, 3) should return [1,2,3]
```
They should also work when used together, for example:
```ruby
(1..100).to_a.even.in_range(18..30) # should return [18, 20, 22, 24, 26, 28, 30]
```
```javascript
[1,2,18,19,20,21,22,30,40,50,100].even().inRange(18,30) // should return [18, 20, 22, 30]
```
```python
list(list([1,2,3,4,5,6,7,8,9,10]).even()).under(5) # should return [2,4]
```

And finally the filters should only accept integer values from an array, for example:
```ruby
["a", 1, "b", 300, "x", "q", 63, 122, 181, "z", 0.83, 0.11].even # should return [300, 122]
```
```javascript
["a", 1, "b", 300, "x", "q", 63, 122, 181, "z", 0.83, 0.11].even() // should return [300, 122]
```
```python
list(["a", 1, "b", 300, "x", "q", 63, 122, 181, "z", 0.83, 0.11]).even() // should return [300, 122]
```

Note: List with non-numbers will be tested as well.
