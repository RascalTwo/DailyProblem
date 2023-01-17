[_metadata_:generated]: - "true"

# Combinator Flip

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`541b5694204d12573700101c`](https://www.codewars.com/kata/541b5694204d12573700101c) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Create a combinator function named flip that takes a function as an argument and returns that function with it's arguments reversed. 

For example:

```javascript
flip(print)(4,5) // returns "5 -> 4"
```
```javascript
function print(a,b) {
  return a + " -> " + b;
}
```

```coffeescript
file(print)(4,5) # return '5 -> 4'
```

```coffeescript
print = (a,b) ->
  a + ' -> ' + b
```
The idea is to reverse any number of arguments using a higher order function, without any concern for the function being passed into it. 


