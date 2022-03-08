[_metadata_:generated]: - "true"

# Battle of the characters (Easy)

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`595519279be6c575b5000016`](https://www.codewars.com/kata/595519279be6c575b5000016) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

### Description:
  Groups of characters decided to make a battle. Help them to figure out which group is more powerful. Create a function that will accept 2 strings and return the one who's stronger.

### Rules:
* Each character have its own power: `A = 1, B = 2, ... Y = 25, Z = 26`
* Strings will consist of uppercase letters only
* Only two groups to a fight.
* Group whose total power (`A + B + C + ...`) is bigger wins.
* If the powers are equal, it's a tie.

### Examples:
```javascript
  battle("ONE", "TWO"); // => "TWO"`
  battle("ONE", "NEO"); // => "Tie!"
```

### Related kata:
- [Battle of the characters (Medium)](https://www.codewars.com/kata/595e9f258b763bc2d2000032)
