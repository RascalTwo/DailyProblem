[_metadata_:generated]: - "true"

# Battle of the characters (Medium)

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`595e9f258b763bc2d2000032`](https://www.codewars.com/kata/595e9f258b763bc2d2000032) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Groups of characters decided to make a battle. Help them to figure out what group is more powerful. Create a function that will accept 2 variables and return the one who's stronger.

### Rules

* Each character has its own power:
  ```
    A = 1, B = 2, ... Y = 25, Z = 26
    a = 0.5, b = 1, ... y = 12.5, z = 13
  ```
* Only alphabetical characters can and will participate in a battle.
* Only two groups to a fight.
* Group whose total power (`a + B + c + ...`) is bigger wins.
* If the powers are equal, it's a tie.

### Examples
```
"One", "Two"  -->  "Two"
"ONE", "NEO"  -->  "Tie!"
```

### Related kata
- [Battle of the characters (Easy)](https://www.codewars.com/kata/595519279be6c575b5000016)
