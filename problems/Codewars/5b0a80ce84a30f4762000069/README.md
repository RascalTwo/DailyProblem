[_metadata_:generated]: - "true"

# FIXME: Hello

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5b0a80ce84a30f4762000069`](https://www.codewars.com/kata/5b0a80ce84a30f4762000069) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

The code provided has a method `hello` which is supposed to show only those attributes which have been *explicitly* set. Furthermore, it is supposed to say them in the *same order* they were set.

But it's not working properly.

# Notes

There are 3 attributes
* name 
* age
* sex ('M' or 'F')

When the same attribute is assigned multiple times the `hello` method shows it only once. If this happens the *order* depends on the **first** assignment of that attribute, but the *value* is from the **last** assignment.

# Examples

* `Hello.`
* `Hello. My name is Bob. I am 27. I am male.`
* `Hello. I am 27. I am male. My name is Bob.`
* `Hello. My name is Alice. I am female.`
* `Hello. My name is Batman.`

# Task
Fix the code so we can all go home early.

