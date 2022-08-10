[_metadata_:generated]: - "true"

# Game Hit the target

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5ffc226ce1666a002bf023d2`](https://www.codewars.com/kata/5ffc226ce1666a002bf023d2) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

<h1>Hit the target</h1>
given a matrix <code>n x n</code> (2-7), determine if the arrow is directed to the target (x). <br>
There will be only 1 arrow '>' and 1 target 'x'<br>
An empty spot will be denoted by a space " ", the target with a cross "x", and the scope ">"
<h2>Examples:</h2>
given matrix 4x4: <br>
  <code>[<br>
  [' ', ' ', ' ', ' '],<br>
  [' ', ' ', ' ', ' '], --> return true<br>
  [' ', '>', ' ', 'x'],<br>
  [' ', ' ', ' ', ' ']<br>
] </code><br>
given matrix 4x4: <br>
  <code>[<br>
  [' ', ' ', ' ', ' '],<br>
  [' ', '>', ' ', ' '], --> return false<br>
  [' ', ' ', ' ', 'x'],<br>
  [' ', ' ', ' ', ' ']<br>
] </code><br>

given matrix 4x4: <br>
  <code>[<br>
  [' ', ' ', ' ', ' '],<br>
  [' ', 'x', '>', ' '], --> return false<br>
  [' ', '', ' ', ' '],<br>
  [' ', ' ', ' ', ' ']<br>
] </code>


In this example, only a 4x4 matrix was used, the problem will have matrices of dimensions from 2 to 7<br>
Happy hacking as they say!
