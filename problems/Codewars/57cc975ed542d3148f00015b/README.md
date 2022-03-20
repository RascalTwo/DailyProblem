[_metadata_:generated]: - "true"

# You only need one - Beginner

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`57cc975ed542d3148f00015b`](https://www.codewars.com/kata/57cc975ed542d3148f00015b) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You will be given an array `a` and a value `x`. All you need to do is check whether the provided array contains the value.

~~~if:swift
The type of `a` and `x` can be `String` or `Int`.
~~~
~~~if-not:swift
Array can contain numbers or strings. X can be either.
~~~
~~~if:racket
In racket, you'll be given a list instead of an array. If the value is in the list,
return #t instead of another value that is also considered true.
```racket
(contains '(1 2 3) 3) ; returns #t
(contains '(1 2 3) 5) ; returns #f
```
~~~

Return `true` if the array contains the value, `false` if not. 
