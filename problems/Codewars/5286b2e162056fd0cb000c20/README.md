[_metadata_:generated]: - "true"

# Collatz

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5286b2e162056fd0cb000c20`](https://www.codewars.com/kata/5286b2e162056fd0cb000c20) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

## Preface

A collatz sequence, starting with a positive integer<i>n</i>, is found by repeatedly applying the following function to <i>n</i> until <i>n</i> == 1 :

`$f(n) =
\begin{cases}
n/2,   \text{  if $n$ is even} \\
3n+1,  \text{  if $n$ is odd}
\end{cases}$`
----

A more detailed description of the collatz conjecture may be found [on Wikipedia](http://en.wikipedia.org/wiki/Collatz_conjecture).

## The Problem

Create a function `collatz` that returns a collatz sequence string starting with the positive integer argument passed into the function, in the following form:

"X<sub>0</sub>->X<sub>1</sub>->...->X<sub>N</sub>"

Where X<sub>i</sub> is each iteration of the sequence and N is the length of the sequence.

## Sample Input

```
Input: 4
Output: "4->2->1"

Input: 3
Output: "3->10->5->16->8->4->2->1"
```

Don't worry about invalid input. Arguments passed into the function are guaranteed to be valid integers >= 1.

