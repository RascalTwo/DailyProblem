[_metadata_:generated]: - "true"

# Find character

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5817030088ca96c0b7000083`](https://www.codewars.com/kata/5817030088ca96c0b7000083) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

>When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own, to enjoy the process  --myjinxin2015 said

# Description:
 
 Give you a character matrix. Find out the character which has the smallest amount.
 
 
 - Arguments:
 
   - `matrix`:  A string that contains some letters. Each row is separated by "\n".
 
 - Results & Note: 
   - Returns the characters which has smallest amount, using string format.
   - If more than one characters are found, sort them according to the order A-Za-z0-9.
   - You can assume that there are at least two characters in the matrix.
   - Please ignore the "\n" ;-)
   
# Some Examples

```
matrix=
00000000
0000O000
00000000
00000000
00000000
findCharacters(matrix) === "O"


matrix=
mmmmmmmmmmmmm
mmmmmmmmmmmmm
mmmmmmmmmmmmm
mmmmmmmmmnmmm
findCharacters(matrix) === "n"

matrix=
AAAAAAAAAAA
AABBBBBBBBB
BCCCCCCCCDD
DDDDEEEEFFF
findCharacters(matrix) === "F"

matrix=
AAAAA
ABBBB
BCCCC
DDDDE
EEEEF
FFFFF
findCharacters(matrix) === "CD"
```

