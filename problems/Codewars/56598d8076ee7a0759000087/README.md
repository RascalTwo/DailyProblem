[_metadata_:generated]: - "true"

# Tip Calculator

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`56598d8076ee7a0759000087`](https://www.codewars.com/kata/56598d8076ee7a0759000087) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Complete the function, which calculates how much you need to tip based on the total amount of the bill and the service. 

You need to consider the following ratings:

- Terrible: tip 0%
- Poor: tip 5%
- Good: tip 10%
- Great: tip 15%
- Excellent: tip 20%

The rating is **case insensitive** (so "great" = "GREAT"). If an unrecognised rating is received, then you need to return:

* `"Rating not recognised"` in Javascript, Python and Ruby...
* ...or `null` in Java
* ...or `-1` in C#

Because you're a nice person, you **always round up** the tip, regardless of the service.

