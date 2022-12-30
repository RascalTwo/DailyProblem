[_metadata_:generated]: - "true"

# Game Hit the target - 2nd part

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`6177b4119b69a40034305f14`](https://www.codewars.com/kata/6177b4119b69a40034305f14) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

<h1 align="center">Hit the target</h1>
<em>This is the second part of the kata :3 🎈🎆🎇🎆🎈</em><br>
given a matrix <code>n x n</code> (2-7), determine if the arrow is directed to the target (x). <br>
Now there are one of 4 types of arrows (<code> '^', '&gt;', 'v', '&lt;' </code>) and only one target (<code>x</code>)<br>
An empty spot will be denoted by a space " ", the target with a cross "x", and the scope ">"
<h2>Examples:</h2>
given matrix 4x4: <br>
  <code>[<br>
  [' ', 'x', ' ', ' '],<br>
  [' ', ' ', ' ', ' '], --> return true<br>
  [' ', '^', ' ', ' '],<br>
  [' ', ' ', ' ', ' ']<br>
] </code><br>
given matrix 4x4: <br>
  <code>[<br>
  [' ', ' ', ' ', ' '],<br>
  [' ', 'v', ' ', ' '], --> return false<br>
  [' ', ' ', ' ', 'x'],<br>
  [' ', ' ', ' ', ' ']<br>
] </code><br>

given matrix 4x4: <br>
  <code>[<br>
  [' ', ' ', ' ', ' '],<br>
  ['>', ' ', ' ', 'x'], --> return true<br>
  [' ', '', ' ', ' '],<br>
  [' ', ' ', ' ', ' ']<br>
] </code>


In this example, only a 4x4 matrix was used, the problem will have matrices of dimensions from 2 to 7<br>
And here is the first part of this kata - <a href='https://www.codewars.com/kata/5ffc226ce1666a002bf023d2'>click me ●v●</a><br>
Happy hacking as they say! 💻

