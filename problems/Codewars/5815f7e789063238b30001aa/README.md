[_metadata_:generated]: - "true"

# Wealth equality, finally!

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5815f7e789063238b30001aa`](https://www.codewars.com/kata/5815f7e789063238b30001aa) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

The year is 2088 and the Radical Marxist Socialist People's Party (RMSPP) has just seized power in Brazil.

Their first act in power is absolute wealth equality through coercive redistribution.

Create a function that redistributes all wealth equally among all citizens.

Wealth is represented as an array/list where every index is the wealth of a single citizen.  
The function should mutate the input such that every index has the same amount of wealth.  

See example:

* Input:
```text
[5, 10, 6]  >>> This represents:
             # citizen 1 has wealth 5
             # citizen 2 has wealth 10
             # citizen 3 has wealth 6
```
* Should be after the test:
```text
 [7, 7, 7] >>> wealth has now been equally redistributed
```

Info:

- **MUTATE the input array/list, don't return anything**
- Input is guaranteed to hold at least 1 citizen
- Wealth of a citizen will be an integer with minimum equal to 0 (negative wealth is not possible)
- Handling of floating point error will not be tested

