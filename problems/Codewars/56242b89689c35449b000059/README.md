[_metadata_:generated]: - "true"

# draw me a chessboard

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`56242b89689c35449b000059`](https://www.codewars.com/kata/56242b89689c35449b000059) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

A grid is a perfect starting point for many games (Chess, battleships, Candy Crush!).

Making a digital chessboard I think is an interesting way of visualising how loops can work together.

Your task is to write a function that takes two integers `rows` and `columns` and returns a chessboard pattern as a two dimensional array.

So `chessBoard(6,4)` should return an array like this:


    [
	    ["O","X","O","X"],
	    ["X","O","X","O"],
	    ["O","X","O","X"],
	    ["X","O","X","O"],
	    ["O","X","O","X"],
	    ["X","O","X","O"]
    ]

And `chessBoard(3,7)` should return this:


    [
    	["O","X","O","X","O","X","O"],
    	["X","O","X","O","X","O","X"],
    	["O","X","O","X","O","X","O"]
    ]

The white spaces should be represented by an: `'O'`

and the black an: `'X'`

The first row should always start with a white space `'O'`

