[_metadata_:generated]: - "true"

# Birthday II - Presents

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5805f0663f1f9c49be00011f`](https://www.codewars.com/kata/5805f0663f1f9c49be00011f) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Your colleagues have been good enough(?) to buy you a birthday gift. Even though it is your birthday and not theirs, they have decided to play pass the parcel with it so that everyone has an even chance of winning. There are multiple presents, and you will receive one, but not all are nice... One even explodes and covers you in soil... strange office. To make up for this one present is a dog! Happy days! (do not buy dogs as presents, and if you do, never wrap them).

Depending on the number of passes in the game (y), and the present you unwrap (x), return as follows:

x == goodpresent --> return x with num of passes added to each charCode (turn to charCode, add y to each, turn back)<br><br>
x == crap || x == empty --> return string sorted alphabetically<br><br>
x == bang --> return string turned to char codes, each code reduced by number of passes and summed to a single figure<br><br>
x == badpresent --> return 'Take this back!'<br><br>
x == dog, return 'pass out from excitement y times' (where y is the value given for y).
