[_metadata_:generated]: - "true"

# Nickname Generator

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`593b1909e68ff627c9000186`](https://www.codewars.com/kata/593b1909e68ff627c9000186) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Nickname Generator

Write a function, `nicknameGenerator` that takes a string name as an argument and returns the first 3 or 4 letters as a nickname.

If the 3rd letter is a consonant, return the first 3 letters.

```javascript
nickname("Robert") //=> "Rob"
nickname("Kimberly") //=> "Kim"
nickname("Samantha") //=> "Sam"
```

If the 3rd letter is a vowel, return the first 4 letters. 

```javascript
nickname("Jeannie") //=> "Jean"
nickname("Douglas") //=> "Doug"
nickname("Gregory") //=> "Greg"
```

If the string is less than 4 characters, return "Error: Name too short".

**Notes:**

- Vowels are "aeiou", so discount the letter "y".
- Input will always be a string.
- Input will always have the first letter capitalised and the rest lowercase (e.g. Sam).
- The input can be modified

