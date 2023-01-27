[_metadata_:generated]: - "true"

# Simple string indices

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5a24254fe1ce0ec2eb000078`](https://www.codewars.com/kata/5a24254fe1ce0ec2eb000078) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

In this Kata, you will be given a string with brackets and an index of an opening bracket and your task will be to return the index of the matching closing bracket.  Both the input and returned index are 0-based **except in Fortran where it is 1-based**. An opening brace will always have a closing brace. Return `-1` if there is no answer (in Haskell, return `Nothing`; in Fortran, return `0`; in Go, return an error)

### Examples

```c
solve("((1)23(45))(aB)", 0) = 10 // the opening brace at index 0 matches the closing brace at index 10
solve("((1)23(45))(aB)", 1) = 3 
solve("((1)23(45))(aB)", 2) = -1 // there is no opening bracket at index 2, so return -1
solve("((1)23(45))(aB)", 6) = 9
solve("((1)23(45))(aB)", 11) = 14
solve("((>)|?(*'))(yZ)", 11) = 14
```

```python
solve("((1)23(45))(aB)", 0) = 10 -- the opening brace at index 0 matches the closing brace at index 10
solve("((1)23(45))(aB)", 1) = 3 
solve("((1)23(45))(aB)", 2) = -1 -- there is no opening bracket at index 2, so return -1
solve("((1)23(45))(aB)", 6) = 9
solve("((1)23(45))(aB)", 11) = 14
solve("((>)|?(*'))(yZ)", 11) = 14
```

```haskell
solve("((1)23(45))(aB)", 0) = Just 10 -- the opening brace at index 0 matches the closing brace at index 10
solve("((1)23(45))(aB)", 2) = Nothing -- there is no opening bracket at index 2, so return "Nothing" instead of -1
```
```fortran
solve("((1)23(45))(aB)", 1) ! => 11 (the opening brace at index 1 matches the closing brace at index 11)
solve("((1)23(45))(aB)", 2) ! => 4
solve("((1)23(45))(aB)", 3) ! => 0 (there is no opening bracket at index 3, so return 0)
solve("((1)23(45))(aB)", 7) ! => 10
solve("((1)23(45))(aB)", 12) ! => 15
solve("((>)|?(*'))(yZ)", 12) ! => 15
```

Input will consist of letters, numbers and special characters, but no spaces. The only brackets will be `(` and `)`. 

More examples in the test cases. 

Good luck!

~~~if:fortran
*NOTE: In Fortran, you may assume that the input string will not contain any leading/trailing whitespace.*
~~~
