[_metadata_:generated]: - "true"

# Exclusive "or" (xor) Logical Operator

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`56fa3c5ce4d45d2a52001b3c`](https://www.codewars.com/kata/56fa3c5ce4d45d2a52001b3c) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Exclusive "or" (xor) Logical Operator

## Overview

In some scripting languages like PHP, there exists a logical operator (e.g. ```&&```, ```||```, ```and```, ```or```, etc.) called the "Exclusive Or" (hence the name of this Kata).  The exclusive or evaluates two booleans.  It then returns true if **exactly one of the two expressions are true**, false otherwise.  For example:


```php
false xor false == false // since both are false
true xor false == true // exactly one of the two expressions are true
false xor true == true // exactly one of the two expressions are true
true xor true == false // Both are true.  "xor" only returns true if EXACTLY one of the two expressions evaluate to true.
```

## Task

Since we cannot define keywords in Javascript (well, at least I don't know how to do it), your task is to define a function ```xor(a, b)``` where a and b are the two expressions to be evaluated.  Your ```xor``` function should have the behaviour described above, returning true if **exactly one of the two expressions evaluate to true**, false otherwise.

