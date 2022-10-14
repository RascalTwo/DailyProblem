[_metadata_:generated]: - "true"

# Numericals of a String

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5b4070144d7d8bbfe7000001`](https://www.codewars.com/kata/5b4070144d7d8bbfe7000001) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You are given an input string.

For each symbol in the string if it's the first character occurrence, replace it with a '1', else replace it with the amount of times you've already seen it.

___

## Examples:

```
input   =  "Hello, World!"
result  =  "1112111121311"

input   =  "aaaaaaaaaaaa"
result  =  "123456789101112"
```

There might be some non-ascii characters in the string.

<hr>

~~~if:java
Note: there will be no int domain overflow (character occurrences will be less than 2 billion).
~~~
~~~if:c
(this does not apply to the C language translation)
~~~


Take note of **performance**

