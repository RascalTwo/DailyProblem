[_metadata_:generated]: - "true"

# Trimming a string

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`563fb342f47611dae800003c`](https://www.codewars.com/kata/563fb342f47611dae800003c) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Return a function that will trim a string (the first argument given) if it is longer than the maximum string length (the second argument given). The result should also end with "..."

These dots at the end also add to the string length.

So in the above example, ```trim("Creating kata is fun", 14)``` should return ```"Creating ka..."```

If the string is smaller than or equal to 3 characters then the length of the dots is not added to the string length.

e.g. ```trim("He", 1)``` should return ```"H..."```

If the string is smaller or equal than the maximum string length, then simply return the string with no trimming or dots required.

e.g. ```trim("Code Wars is pretty rad", 50)``` should return ```"Code Wars is pretty rad"```

