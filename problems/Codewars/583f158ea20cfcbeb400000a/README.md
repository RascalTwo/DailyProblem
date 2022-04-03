[_metadata_:generated]: - "true"

# Make a function that does arithmetic!

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`583f158ea20cfcbeb400000a`](https://www.codewars.com/kata/583f158ea20cfcbeb400000a) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them. 


```a``` and ```b``` will both be positive integers, and ```a``` will always be the first number in the operation, and ```b``` always the second.

The four operators are "add", "subtract", "divide", "multiply". 

~~~if-not:haskell
A few **examples:(Input1, Input2, Input3 --> Output)**
```
5, 2, "add"      --> 7
5, 2, "subtract" --> 3
5, 2, "multiply" --> 10
5, 2, "divide"   --> 2.5
```
~~~

~~~if:haskell
In **Haskell**:

  1. The operation is defined as
```haskell
data Operation = Add | Divide | Multiply | Subtract deriving (Eq, Show, Enum, Bounded)
```
  2. The arithmetic function as 
```haskell
arithmetic :: Double -> Double -> Operation -> Double
arithmetic :: Fractional a => a -> a -> Operation -> a
```
~~~


Try to do it without using if statements!

