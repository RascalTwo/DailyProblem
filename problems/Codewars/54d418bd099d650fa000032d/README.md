[_metadata_:generated]: - "true"

# Vampire Numbers

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`54d418bd099d650fa000032d`](https://www.codewars.com/kata/54d418bd099d650fa000032d) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

----
Vampire Numbers
----

Our loose definition of [Vampire Numbers](http://en.wikipedia.org/wiki/Vampire_number) can be described as follows:

```python
6 * 21 = 126
# 6 and 21 would be valid 'fangs' for a vampire number as the 
# digits 6, 1, and 2 are present in both the product and multiplicands

10 * 11 = 110
# 110 is not a vampire number since there are three 1's in the
# multiplicands, but only two 1's in the product
```

Create a function that can receive two 'fangs' and determine if the product of the two is a valid vampire number.

