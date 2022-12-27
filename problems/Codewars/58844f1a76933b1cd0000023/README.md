[_metadata_:generated]: - "true"

# Simple Fun #8: Kill K-th Bit

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`58844f1a76933b1cd0000023`](https://www.codewars.com/kata/58844f1a76933b1cd0000023) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

## Task
 In order to stop the Mad Coder evil genius you need to decipher the encrypted message he sent to his minions. The message contains several numbers that, when typed into a supercomputer, will launch a missile into the sky blocking out the sun, and making all the people on Earth grumpy and sad.

 You figured out that some numbers have a modified single digit in their binary representation. More specifically, in the given number `n` the `k`<sup>th</sup> bit from the right was initially set to 0, but its current value might be different. It's now up to you to write a function that will change the `k`<sup>th</sup> bit of `n` back to 0.

## Example

 For n = 37 and k = 3, the output should be `33`.

 37<sub>10</sub> = 100<font color='red'>1</font>01<sub>2</sub> ~> 100<font color='red'>0</font>01<sub>2</sub> = 33<sub>10</sub>

 For n = 37 and k = 4, the output should be 37.

 The 4<sup>th</sup> bit is 0 already (looks like the Mad Coder forgot to encrypt this number), so the answer is still 37.

## Input/Output

 - `[input]` integer `n`

 Constraints: 0 ≤ n ≤ 2<sup>31</sup> - 1.

 - `[input]` integer `k`

 The `1-based` index of the changed bit (`counting from the right`).

 Constraints: 1 ≤ k ≤ 31.

 - `[output]` an integer
## More Challenge
 - Are you a One-Liner? Please try to complete the kata in one line(no test for it) ;-)
