[_metadata_:generated]: - "true"

# Simple Fun #23: Square Digits Sequence

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5886d65e427c27afeb0000c1`](https://www.codewars.com/kata/5886d65e427c27afeb0000c1) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Task
 Consider a sequence of numbers a<sub>0</sub>, a<sub>1</sub>, ..., a<sub>n</sub>, in which an element is equal to the sum of squared digits of the previous element. The sequence ends once an element that has already been in the sequence appears again.

 Given the first element `a0`, find the length of the sequence.

# Example

 For a0 = 16, the output should be `9`

 Here's how elements of the sequence are constructed:

 a0 = 16

 a1 = 1<sup>2</sup> + 6<sup>2</sup> = 37

 a2 = 3<sup>2</sup> + 7<sup>2</sup> = 58

 a3 = 5<sup>2</sup> + 8<sup>2</sup> = 89

 a4 = 8<sup>2</sup> + 9<sup>2</sup> = 145

 a5 = 1<sup>2</sup> + 4<sup>2</sup> + 5<sup>2</sup> = 42

 a6 = 4<sup>2</sup> + 2<sup>2</sup> = 20

 a7 = 2<sup>2</sup> + 0<sup>2</sup> = 4

 a8 = 4<sup>2</sup> = 16, which has already occurred before (a0)

 Thus, there are 9 elements in the sequence.

 For a0 = 103, the output should be `4`

 The sequence goes as follows: 103 -> 10 -> 1 -> 1, 4 elements altogether.

# Input/Output

 - `[input]` integer `a0`

    First element of a sequence, positive integer.

    Constraints: 1 ≤ a0 ≤ 650.

 - `[output]` an integer
