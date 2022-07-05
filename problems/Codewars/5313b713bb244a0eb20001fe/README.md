[_metadata_:generated]: - "true"

# Number-like counter

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5313b713bb244a0eb20001fe`](https://www.codewars.com/kata/5313b713bb244a0eb20001fe) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You're going to implement a simple counter class. The counter will start at zero, and every time its `incr` method is called, it will increase by 1.

**There's one caveat:** Your counter must act like a number and support arithmetic operations and comparisons.

For example:

    var c = new Counter();
    c.incr(); // counter is now at 1
    c + 1; // 2
    c > 1; // false
    c > 0; // true
    c == 1; // true
    Math.sqrt(c); // 1

You are not required to support equality comparison between two `Counter` instances.
