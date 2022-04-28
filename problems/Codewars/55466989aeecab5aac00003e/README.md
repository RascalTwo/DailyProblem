[_metadata_:generated]: - "true"

# Rectangle into Squares

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`55466989aeecab5aac00003e`](https://www.codewars.com/kata/55466989aeecab5aac00003e) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

The drawing below gives an idea of how to cut a given "true" rectangle into squares ("true" rectangle meaning that the two dimensions are different).

![alternative text](https://i.imgur.com/lk5vJ7sm.jpg)

Can you translate this drawing into an algorithm?

You will be given two dimensions 

1. a positive integer length
2. a positive integer width

You will return a collection or a string (depending on the language; Shell bash, PowerShell, Pascal and Fortran return a string) with the size of each of the  squares.
#### Examples in general form:
(depending on the language)
```
  sqInRect(5, 3) should return [3, 2, 1, 1]
  sqInRect(3, 5) should return [3, 2, 1, 1]
  
  You can see examples for your language in **"SAMPLE TESTS".**
```

#### Notes:
- `lng == wdth` as a starting case would be an entirely different problem and the drawing is planned to be interpreted with `lng != wdth`. (See kata, Square into Squares. Protect trees! http://www.codewars.com/kata/54eb33e5bc1a25440d000891 for this problem). 

  When the initial parameters are so that `lng` == `wdth`, the solution `[lng]` would be the most obvious but not in the spirit of this kata   so, in that case, return `None`/`nil`/`null`/`Nothing` **or**
  return `{}` with C++, `Array()` with Scala, `[]` with Perl, Raku.
 - In that case the returned structure of **C** will have its `sz` component equal to `0`. 
 - Return the string `"nil"` with Bash, PowerShell, Pascal and Fortran.




