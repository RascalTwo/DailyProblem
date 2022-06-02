[_metadata_:generated]: - "true"

# Array#reduce

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5411e3e95f3a7f6a7a0000e3`](https://www.codewars.com/kata/5411e3e95f3a7f6a7a0000e3) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

In this kata, you must define the `Array.reduce` method.

_I have disabled the pre-existing reduce methods._

Here's how it works:
```javascript
[1,2,3].reduce( function(sum, next){return sum+next}, 0) 
// => 6

['a','b','a'].reduce( function(obj, elem){if(!obj[elem]) obj[elem] = 0; obj[elem] += 1; return obj}, {})
// => {'a':2, 'b':1}
```
```ruby
[1,2,3].reduce( ->(x,y){x+y}, 0) 
# => 6
```
```coffeescript
[1 2 3].reduce((sum, next) -> sum + next , 0)
# => 6

["a" "b" "a" ].reduce ((obj, elem) ->
  obj[elem] = 0  unless obj[elem]
  obj[elem] += 1
  obj), {}
# => {'a':2, 'b':1}
```
__Summary:__ The `reduce` method goes through each element of an array, applies the function to whatever the function returned last, and returns the last outcome. On the first iteration, it should pass the `initial` value to the function, as well as the first element of the array. If no `initial` value is passed, skip to the first element of the array.

Ruby methods should expect a lambda.
