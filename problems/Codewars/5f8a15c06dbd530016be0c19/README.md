[_metadata_:generated]: - "true"

# Duplicate sandwich

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5f8a15c06dbd530016be0c19`](https://www.codewars.com/kata/5f8a15c06dbd530016be0c19) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

## Task

In this kata you will be given a list consisting of unique elements except for one thing that appears twice.

Your task is to output a list of everything inbetween both occurrences of this element in the list.

## Examples:

```python
[0, 1, 2, 3, 4, 5, 6, 1, 7, 8] => [2, 3, 4, 5, 6]
['None', 'Hello', 'Example', 'hello', 'None', 'Extra'] => ['Hello', 'Example', 'hello']
[0, 0] => []
[True, False, True] => [False]
['e', 'x', 'a', 'm', 'p', 'l', 'e'] => ['x', 'a', 'm', 'p', 'l']
```
```haskell
[0, 1, 2, 3, 4, 5, 6, 1, 7, 8] -> [2, 3, 4, 5, 6]
["None", "Hello", "Example", "hello", "None", "Extra"] -> ["Hello", "Example", "hello"]
[0, 0] -> []
[True, False, True] -> [False]
"example" -> "xampl"
```
```javascript
[0, 1, 2, 3, 4, 5, 6, 1, 7, 8] => [2, 3, 4, 5, 6]
["None", "Hello", "Example", "hello", "None", "Extra"] => ["Hello", "Example", "hello"]
[0, 0] => []
[true, false, true] => [false]
"example" => "xampl"
```

## Notes

* All elements will be the same datatype.

~~~if:python
* All used elements will be hashable.
~~~

~~~if:javascript
* All used elements will be primitive.
~~~
