[_metadata_:generated]: - "true"

# Unpacking Arguments

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`540de1f0716ab384b4000828`](https://www.codewars.com/kata/540de1f0716ab384b4000828) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You must create a function, `spread`, that takes a function and a list of arguments to be applied to that function. You must make this function return the result of calling the given function/lambda with the given arguments.

eg:
```javascript
spread(someFunction, [1, true, "Foo", "bar"] ) 
// is the same as...
someFunction(1, true, "Foo", "bar")
```
```clojure
(spread someFunction [1 true "Foo" "bar"] ) 
; is the same as...
(someFunction 1 true "Foo" "bar")
```
```coffeescript
spread someFunction, [1, true, "Foo", "bar"] 
# is the same as...
someFunction 1, true, "Foo", "bar" 
```
```python
spread(someFunction, [1, true, "Foo", "bar"] ) 
# is the same as...
someFunction(1, true, "Foo", "bar")
```
```ruby
spread someFunction, [1, true, "Foo", "bar"] 
# is the same as...
someFunction.(1, true, "Foo", "bar")
```
