[_metadata_:generated]: - "true"

# Lazily executing a function

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5458d4d2cbae2a9438000389`](https://www.codewars.com/kata/5458d4d2cbae2a9438000389) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Deferring a function execution can sometimes save a lot of execution time in our programs by *postponing* the execution to the latest possible instant of time, when we're sure that the time spent while executing it is worth it.

Write a method `make_lazy` that takes in a function (symbol for Ruby) and the arguments to the function and returns another function (lambda for Ruby) which when invoked, returns the result of the original function invoked with the supplied arguments.

For example:

Given a function `add`

    function add (a, b) {
      return a + b;
    }

One could make it *lazy* as:

    var lazy_value = make_lazy(add, 2, 3);
    
The expression does not get evaluated at the moment, but only when you *invoke* `lazy_value` as:

    lazy_value() => 5
    
The above invokation then performs the sum.

Please note: The functions that are passed to `make_lazy` may take one or more arguments and the number of arguments is not fixed.
