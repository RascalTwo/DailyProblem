[_metadata_:generated]: - "true"

# Strings: starts with

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                        |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5803a6d8db07c59fff00015f`](https://www.codewars.com/kata/5803a6d8db07c59fff00015f) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

Challenge:
Given two null-terminated strings in the arguments "string" and "prefix", determine if "string" starts with the "prefix" string. Return true or false.

Example:
```
startsWith("hello world!", "hello"); // should return true
startsWith("hello world!", "HELLO"); // should return false
startsWith("nowai", "nowaisir"); // should return false
```

Addendum:
For this problem, an empty "prefix" string should always return true for any value of "string".

If the length of the "prefix" string is greater than the length of the "string", return false.

The check should be case-sensitive, i.e. startsWith("hello", "HE") should return false, whereas startsWith("hello", "he") should return true.

The length of the "string" as well as the "prefix" can be defined by the formula: <i>0 <= length < +Infinity</i>

No characters should be ignored and/or omitted during the test, e.g. whitespace characters should not be ignored.
