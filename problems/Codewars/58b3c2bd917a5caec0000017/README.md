[_metadata_:generated]: - "true"

# Simple Fun #170: Sum Groups

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`58b3c2bd917a5caec0000017`](https://www.codewars.com/kata/58b3c2bd917a5caec0000017) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Task

Given an array of integers, sum consecutive even numbers and consecutive odd numbers. Repeat the process while it can be done and return the length of the final array.

# Example

For `arr = [2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9]`
 
The result should be `6`.

```
[2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9]  -->
         2+2+6       0+2+0     5+5+7+7       3+3+9
[2, 1,   10,    5,    2,        24,     4,   15   ] -->
                               2+24+4
[2, 1,   10,    5,             30,           15   ]
The length of final array is 6
```

# Input/Output

- `[input]` integer array `arr`

  A non-empty array, 

  `1 ≤ arr.length ≤ 1000`

  `0 ≤ arr[i] ≤ 1000`


- `[output]` an integer

  The length of the final array

~~~if:lambdacalc
# Encodings

purity: `LetRec`  
numEncoding: `BinaryScott`  
export constructors `nil, cons` for your `List` encoding  
~~~
