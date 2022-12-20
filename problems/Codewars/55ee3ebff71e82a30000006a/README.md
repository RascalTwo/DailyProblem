[_metadata_:generated]: - "true"

# Excel sheet column numbers

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`55ee3ebff71e82a30000006a`](https://www.codewars.com/kata/55ee3ebff71e82a30000006a) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Write a function 

`titleToNumber(title) or title_to_number(title) or titleToNb title ...`

(depending on the language)

that given a column title as it appears in an Excel sheet, returns its corresponding column number. All column titles will be uppercase.

Examples:
```
titleTonumber('A') === 1
titleTonumber('Z') === 26
titleTonumber('AA') === 27
```


```clojure
Note for Clojure:
Don't use Java Math/pow (even with bigint) because there is a loss of precision 
when the length of "title" is growing. 
Write your own function "exp [x n]".
```



