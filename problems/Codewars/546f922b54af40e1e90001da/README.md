[_metadata_:generated]: - "true"

# Replace With Alphabet Position

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`546f922b54af40e1e90001da`](https://www.codewars.com/kata/546f922b54af40e1e90001da) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

`"a" = 1`, `"b" = 2`, etc.

## Example <!-- unlisted languages will use the first entry. please keep python up top. -->

```python
alphabet_position("The sunset sets at twelve o' clock.")
```
```javascript
alphabetPosition("The sunset sets at twelve o' clock.")
```
```scala
alphabetPosition("The sunset sets at twelve o' clock.")
```
```haskell
alphabetPosition "The sunset sets at twelve o' clock."
```
```cobol
      AlphabetPosition("The sunset sets at twelve o' clock.")
```
```groovy
Kata.alphabetPosition("The sunset sets at twelve o' clock.")
```
```csharp
Kata.AlphabetPosition("The sunset sets at twelve o' clock.")
```
```nasm
text:  db  "The sunset sets at twelve o' clock.",0h0

main:
    mov rdi, text
    call alphabet_position
```

Should return `"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"` ( as a string )
