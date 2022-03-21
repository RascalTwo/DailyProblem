[_metadata_:generated]: - "true"

# Invert values

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5899dc03bc95b1bf1b0000ad`](https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

~~~if-not:racket
```
invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
```
~~~

```if:javascript,python,ruby,php,elixir,dart
You can assume that all values are integers. Do not mutate the input array/list.
```

```if:c
### Notes:
- All values are greater than `INT_MIN`
- The input should be modified, not returned.
```
~~~if:racket
```racket
(invert '(1 2 3 4 5))   ; '(-1 -2 -3 -4 -5)
(invert '(1 -2 3 -4 5)) ; '(-1 2 -3 4 -5)
(invert '())            ; '()
```
~~~
