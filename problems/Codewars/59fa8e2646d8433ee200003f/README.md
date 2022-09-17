[_metadata_:generated]: - "true"

# Sorting by bits

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`59fa8e2646d8433ee200003f`](https://www.codewars.com/kata/59fa8e2646d8433ee200003f) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

In this kata you're expected to sort an array of 32-bit integers in ascending order of the number of **on** bits they have.

E.g Given the array **[7, 6, 15, 8]**

- 7 has **3 on** bits  (000...0**111**)
- 6 has **2 on** bits  (000...00**11**)
- 15 has **4 on** bits (000...**1111**)
- 8 has **1 on** bit   (000...**1**000)

So the array in sorted order would be **[8, 6, 7, 15]**.

In cases where two numbers have the same number of bits, compare their real values instead.

E.g between 10 **(...1010)** and 12 **(...1100)**, they both have the same number of **on** bits '**2**' but the integer 10 is less than 12 so it comes first in sorted order.

Your task is to write the function `sortBybit()` that takes an array of integers and sort them as described above.

```if-not:haskell
Note: your solution has to sort the array __in place__.
```

Example: 
    
    [3, 8, 3, 6, 5, 7, 9, 1]   =>    [1, 8, 3, 3, 5, 6, 9, 7]

