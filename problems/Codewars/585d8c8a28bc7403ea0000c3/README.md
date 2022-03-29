[_metadata_:generated]: - "true"

# Find the unique string

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`585d8c8a28bc7403ea0000c3`](https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

There is an array of strings. All strings contains similar _letters_ except one. Try to find it!

```javascript
findUniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) === 'BbBb'
findUniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) === 'foo'
```

```php
find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]); // => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]); // => 'foo'
```

```python
find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
```

```cobol
      FindUniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ])
      * => result = 'BbBb'
      FindUniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ])
      * => result = 'foo'
```

Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 3 strings.

This is the second kata in series:

1. [Find the unique number](https://www.codewars.com/kata/585d7d5adb20cf33cb000235)
2. Find the unique string (this kata)
3. [Find The Unique](https://www.codewars.com/kata/5862e0db4f7ab47bed0000e5)
