[_metadata_:generated]: - "true"

# Check if two words are isomorphic to each other

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`59dbab4d7997cb350000007f`](https://www.codewars.com/kata/59dbab4d7997cb350000007f) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Two strings ```a``` and b are called isomorphic if there is a one to one mapping possible for every character of ```a``` to every character of ```b```. And all occurrences of every character in ```a``` map to same character in ```b```.

## Task

In this kata you will create a function that return ```True``` if two given strings are isomorphic to each other, and ```False``` otherwise. Remember that order is important.

Your solution must be able to handle words with more than 10 characters.

## Example
True:
```
CBAABC DEFFED
XXX YYY
RAMBUNCTIOUSLY THERMODYNAMICS
```

False:
```
AB CC
XXY XYY
ABAB CD
```
