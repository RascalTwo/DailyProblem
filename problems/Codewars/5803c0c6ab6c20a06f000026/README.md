[_metadata_:generated]: - "true"

# Strings: swap vowels' case

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5803c0c6ab6c20a06f000026`](https://www.codewars.com/kata/5803c0c6ab6c20a06f000026) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

<i>Special thanks to <b>SteffenVogel_79</b> for the idea</i>.

```if:c
Challenge:

Given a null-terminated string and a pre-allocated buffer that has enough memory to store the full null-terminated copy of the passed string, copy the entire string into the buffer with its vowels' case swapped, and return the pointer to the beginning of the copied string (buffer).
```
```if-not:c
Challenge:

Given a string, return a copy of the string with the vowels' case swapped.
```

For this kata, assume that vowels are in the set `"aeouiAEOUI"`.


```if:c
Example:
Given a string `"C is alive!"` and a buffer of size `strlen("C is alive!") + 1`, after the call to swapCase(), the function should return the pointer to the buffer which now contains `"C Is AlIvE!"` and is properly null-terminated.
```
```if-not:c
Example:
Given a string `"C is alive!"`, your function should return `"C Is AlIvE!"`
```

Addendum:
Your solution is only required to work for the ASCII character set.

Please make sure you only swap cases for the vowels.

```if:c
Your solution should not allocate or de-allocate any memory. The buffer has already been pre-allocated before the call. Dont forget to NUL-terminate the output string.

The buffer has enough memory to hold the passed string and its null terminator entirely.
```
