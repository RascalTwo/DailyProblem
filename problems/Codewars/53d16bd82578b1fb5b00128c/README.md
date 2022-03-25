[_metadata_:generated]: - "true"

# Grader

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`53d16bd82578b1fb5b00128c`](https://www.codewars.com/kata/53d16bd82578b1fb5b00128c) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Create a function that takes a number as an argument and returns a grade based on that number.

Score                                    | Grade
-----------------------------------------|-----
Anything greater than 1 or less than 0.6 | "F"
0.9 or greater                           | "A"
0.8 or greater                           | "B"
0.7 or greater                           | "C"
0.6 or greater                           | "D"

Examples:
```
grader(0)   should be "F"
grader(1.1) should be "F"
grader(0.9) should be "A"
grader(0.8) should be "B"
grader(0.7) should be "C"
grader(0.6) should be "D"
```
