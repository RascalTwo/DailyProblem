[_metadata_:generated]: - "true"

# Replace every nth

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`57fcaed83206fb15fd00027a`](https://www.codewars.com/kata/57fcaed83206fb15fd00027a) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

## Task

Write a method, that replaces every nth char _oldValue_ with char _newValue_.

## Inputs

* `text`: the string to modify
* `n`: change the target letter every `n`<sup>th</sup> occurrencies
* `old_value` (or similar): the targetted character
* `new_value` (or similar): the character to use as replacement

Note for untyped languages: all inputs are always valid and of their expected type.

## Rules

* Your method has to be case sensitive!
* If n is 0 or negative or if it is larger than the count of the oldValue, return the original text without a change.

## Example:
```
n:         2
old_value: 'a'
new_value: 'o'
"Vader said: No, I am your father!"
  1     2          3        4       -> 2nd and 4th occurence are replaced
"Vader soid: No, I am your fother!"
```

As you can see in the example: The first changed is the 2nd 'a'. So the start is always at the nth suitable char and not at the first!
