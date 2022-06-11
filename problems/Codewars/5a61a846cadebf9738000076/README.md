[_metadata_:generated]: - "true"

# Peak array index

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5a61a846cadebf9738000076`](https://www.codewars.com/kata/5a61a846cadebf9738000076) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Given an array of ints, return the index such that the sum of the elements to the right of that index equals the sum of the elements to the left of that index. If there is no such index, return `-1`. If there is more than one such index, return the left-most index.

For example: 
```
peak([1,2,3,5,3,2,1]) = 3, because the sum of the elements at indexes 0,1,2 == sum of elements at indexes 4,5,6. We don't sum index 3.
peak([1,12,3,3,6,3,1]) = 2
peak([10,20,30,40]) = -1
```

```haskell
--For Haskell
peak [1,12,3,3,6,3,1] == Just 2
peak [10,20,30,40]  == Nothing 
```

```cobol
      * For COBOL (1-based index)
      peak [1,12,3,3,6,3,1] =>  3
      peak [10,20,30,40]    => -1
```

The special case of an array of zeros (for instance `[0,0,0,0]`) will not be tested. 

More examples in the test cases. 

Good luck!

Please also try [Simple time difference](https://www.codewars.com/kata/5b76a34ff71e5de9db0000f2)
