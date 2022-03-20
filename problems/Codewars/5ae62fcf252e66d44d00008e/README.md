[_metadata_:generated]: - "true"

# Expressions Matter 

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5ae62fcf252e66d44d00008e`](https://www.codewars.com/kata/5ae62fcf252e66d44d00008e) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Task

* **_Given_** *three integers* `a` ,`b` ,`c`, **_return_** *the **_largest number_** obtained after inserting the following operators and brackets*: `+`, `*`, `()`
* In other words , **_try every combination of a,b,c with [*+()] , and return the Maximum Obtained_**
___
# Consider an Example :

**_With the numbers are 1, 2 and 3_** , *here are some ways of placing signs and brackets*:

* `1 * (2 + 3) = 5`
* `1 * 2 * 3 = 6`
* `1 + 2 * 3 = 7`
* `(1 + 2) * 3 = 9`

So **_the maximum value_** that you can obtain is  **_9_**.

___
# Notes 

* **_The numbers_** *are always* **_positive_**. 
* **_The numbers_** *are in the range* **_(1  ≤  a, b, c  ≤  10)_**.
* *You can use the same operation* **_more than once_**.
* **It's not necessary** *to place all the signs and brackets*.
* **_Repetition_** *in numbers may occur* .
* You **_cannot swap the operands_**. For instance, in the given example **_you cannot get expression_** `(1 + 3) * 2 = 8`.

___
# Input >> Output Examples:

```
expressionsMatter(1,2,3)  ==>  return 9
```
## **_Explanation_**:
*After placing signs and brackets, the **_Maximum value_** obtained from the expression* `(1+2) * 3 = 9`.
___

```
expressionsMatter(1,1,1)  ==>  return 3
```
## **_Explanation_**:
*After placing signs, the **_Maximum value_** obtained from the expression is* `1 + 1 + 1 = 3`.
___

```
expressionsMatter(9,1,1)  ==>  return 18
```
## **_Explanation_**:
*After placing signs and brackets, the **_Maximum value_** obtained from the expression is* `9 * (1+1) = 18`.
___
___
___

# [Playing with Numbers Series](https://www.codewars.com/collections/playing-with-numbers)

# [Playing With Lists/Arrays Series](https://www.codewars.com/collections/playing-with-lists-slash-arrays)

# [Bizarre Sorting-katas](https://www.codewars.com/collections/bizarre-sorting-katas)

# [For More Enjoyable Katas](http://www.codewars.com/users/MrZizoScream/authored)
___

## ALL translations are welcomed

## Enjoy Learning !!
# Zizou




