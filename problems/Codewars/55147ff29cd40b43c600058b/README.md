[_metadata_:generated]: - "true"

# Character Concatenation

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`55147ff29cd40b43c600058b`](https://www.codewars.com/kata/55147ff29cd40b43c600058b) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Given a string, you progressively need to concatenate the first letter from the left and the first letter to the right and "1", then the second letter from the left and the second letter to the right and "2", and so on.

If the string's length is odd drop the central element.

For example:
```python
char_concat("abcdef")    == 'af1be2cd3'
char_concat("abc!def")   == 'af1be2cd3' # same result
```
```javascript
charConcat("abcdef")    == 'af1be2cd3'
charConcat("abc!def")   == 'af1be2cd3' // same result
```
```ruby
char_concat("abcdef")    == 'af1be2cd3'
char_concat("abc!def")   == 'af1be2cd3' # same result
```

