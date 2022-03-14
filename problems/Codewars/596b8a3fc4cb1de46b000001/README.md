[_metadata_:generated]: - "true"

# "Center yourself", says the monk.

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`596b8a3fc4cb1de46b000001`](https://www.codewars.com/kata/596b8a3fc4cb1de46b000001) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Your company **MRE Tech** has hired a spiritual consultant who advised on a
new *Balance* policy: Don't take sides, don't favour, stay in the middle. This
policy even applies to the software where all strings should now be centered.
You are the poor soul to implement it.

# Task

```if-not:c
Implement a function `center` that takes a string `strng`, an integer `width`,
and an optional character `fill` (default: `' '`) and returns a new string of
length `width` where `strng` is centered and on the right and left padded with
`fill`.
```
```if:c
Implement a function `center` that takes a string `strng`, an integer `width`,
and a character `fill` and returns a new string of length `width` where
`strng` is centered and on the right and left padded with `fill`.
```

```python
center(strng, width, fill=' ')
```
```javascript
center(strng, width, fill=' ')
```
```c
char *center(const char *strng, size_t width, char fill)
```

If the left and right padding cannot be of equal length make the padding on the
left side one character longer.

If `strng` is longer than `width` return `strng` unchanged.

# Examples

```python
center('a', 3)  # returns " a "
center('abc', 10, '_')  # returns "____abc___"
center('abcdefg', 2)  # returns "abcdefg"
```
```javascript
center('a', 3)  # returns " a "
center('abc', 10, '_')  # returns "____abc___"
center('abcdefg', 2)  # returns "abcdefg"
```
```c
center("a", 3, ' ')  // returns " a "
center("abc", 10, '_')  // returns "____abc___"
center("abcdefg", 2, ' ')  // returns "abcdefg"
```

