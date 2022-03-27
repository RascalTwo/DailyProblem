[_metadata_:generated]: - "true"

# Thinkful - Number Drills: Blue and red marbles

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5862f663b4e9d6f12b00003b`](https://www.codewars.com/kata/5862f663b4e9d6f12b00003b) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You and a friend have decided to play a game to drill your statistical intuitions. The game works like this:

You have a bunch of red and blue marbles. To start the game you grab a handful of marbles of each color and put them into the bag, keeping track of how many of each color go in. You take turns reaching into the bag, guessing a color, and then pulling one marble out. You get a point if you guessed correctly. The trick is you only have three seconds to make your guess, so you have to think quickly.

You've decided to write a function, `guessBlue()` to help automatically calculate whether you should guess "blue" or "red". The function should take four arguments:

 * the number of blue marbles you put in the bag to start
 * the number of red marbles you put in the bag to start
 * the number of blue marbles pulled out so far (always lower than the starting number of blue marbles)
 * the number of red marbles pulled out so far (always lower than the starting number of red marbles)

`guessBlue()` should return the probability of drawing a blue marble, expressed as a float. For example, `guessBlue(5, 5, 2, 3)` should return `0.6`.
