[_metadata_:generated]: - "true"

# Enumerable Magic #5- True for Just One?

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`54599705cbae2aa60b0011a4`](https://www.codewars.com/kata/54599705cbae2aa60b0011a4) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

## Task

Create a function called `one` that accepts two params:

* a sequence 
* a function

and returns `true` only if the function in the params returns `true` for exactly one (`1`) item in the sequence. 

## Example

```
one([1, 3, 5, 6, 99, 1, 3], bigger_than_ten) -> true
one([1, 3, 5, 6, 99, 88, 3], bigger_than_ten) -> false
one([1, 3, 5, 6, 5, 1, 3], bigger_than_ten) -> false
```

If you need help, [here](http://www.rubycuts.com/enum-one) is a resource ( in Ruby ).
