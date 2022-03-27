[_metadata_:generated]: - "true"

# Quadratic Coefficients Solver

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5d59576768ba810001f1f8d6`](https://www.codewars.com/kata/5d59576768ba810001f1f8d6) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

In this Kata you are expected to find the coefficients of quadratic equation of the given two roots (`x1` and `x2`).

Equation will be the form of ```ax^2 + bx + c = 0```

<b>Return type</b> is a Vector (tuple in Rust, Array in Ruby) containing coefficients of the equations in the order `(a, b, c)`.

Since there are infinitely many solutions to this problem, we fix `a = 1`.

Remember, the roots can be written like `(x-x1) * (x-x2) = 0`

### Example 

    quadratic(1,2) = (1, -3, 2)

This means `(x-1) * (x-2) = 0`; when we do the multiplication this becomes `x^2 - 3x + 2 = 0`

### Example 2

    quadratic(0,1) = (1, -1, 0)

This means `(x-0) * (x-1) = 0`; when we do the multiplication this becomes `x^2 - x + 0 = 0`

### Notes

* Inputs will be integers.
* When `x1 == x2`, this means the root has the multiplicity of two

