[_metadata_:generated]: - "true"

# Snakes and Ladders

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`587136ba2eefcb92a9000027`](https://www.codewars.com/kata/587136ba2eefcb92a9000027) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Introduction

<pre style="white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;">
Snakes and Ladders is an ancient Indian board game regarded today as a worldwide classic. It is played between two or more players on a gameboard having numbered, gridded squares. A number of "ladders" and "snakes" are pictured on the board, each connecting two specific board squares. (Source <a href="https://en.wikipedia.org/wiki/Snakes_and_Ladders">Wikipedia</a>)
</pre>

<center><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/snakesandladders.jpg"></center>

# Task

<pre style="white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;">
Your task is to make a simple class called <font color="#A1A85E">SnakesLadders</font>. The test cases will call the method <font color="#A1A85E">play(die1, die2)</font> independantly of the state of the game or the player turn. The variables <font color="#A1A85E">die1</font> and <font color="#A1A85E">die2</font> are the die thrown in a turn and are both integers between 1 and 6. The player will move the sum of die1 and die2.
</pre>

# The Board
<img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/snakesandladdersboard.jpg">

# Rules
<pre style="white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;">
1.&nbsp; There are two players and both start off the board on square 0.

2.&nbsp; Player 1 starts and alternates with player 2.

3.&nbsp; You follow the numbers up the board in order 1=>100

4.&nbsp; If the value of both die are the same then that player will have another go.

5.&nbsp; Climb up ladders. The ladders on the game board allow you to move upwards and get ahead faster. If you land exactly on a square that shows an image of the bottom of a ladder, then you may move the player all the way up to the square at the top of the ladder. (even if you roll a double).

6.&nbsp; Slide down snakes. Snakes move you back on the board because you have to slide down them. If you land exactly at the top of a snake, slide move the player all the way to the square at the bottom of the snake or chute. (even if you roll a double).

7.&nbsp; Land exactly on the last square to win. The first person to reach the highest square on the board wins. But there's a twist! If you roll too high, your player "bounces" off the last square and moves back. You can only win by rolling the exact number needed to land on the last square. For example, if you are on square 98 and roll a five, move your game piece to 100 (two moves), then "bounce" back to 99, 98, 97 (three, four then five moves.)

8.&nbsp; If the Player rolled a double and lands on the finish square “100” without any remaining moves then the Player wins the game and does not have to roll again.
</pre>


# Returns
<pre style="white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;">
Return <font color="#A1A85E">Player n Wins!</font>. Where n is winning player that has landed on square 100 without any remainding moves left.

Return <font color="#A1A85E">Game over!</font> if a player has won and another player tries to play.

Otherwise return <font color="#A1A85E">Player n is on square x</font>. Where n is the current player and x is the sqaure they are currently on.
</pre>

Good luck and enjoy!

# Kata Series
If you enjoyed this, then please try one of my other Katas. Any feedback, translations and grading of beta Katas are greatly appreciated. Thank you.

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/58663693b359c4a6560001d6" target="_blank">Maze Runner</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/58693bbfd7da144164000d05" target="_blank">Scooby Doo Puzzle</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/7KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/586a1af1c66d18ad81000134" target="_blank">Driving License</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/586c0909c1923fdb89002031" target="_blank">Connect 4</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/586e6d4cb98de09e3800014f" target="_blank">Vending Machine</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/587136ba2eefcb92a9000027" target="_blank">Snakes and Ladders</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/58a848258a6909dd35000003" target="_blank">Mastermind</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/58b2c5de4cf8b90723000051" target="_blank">Guess Who?</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/58f5c63f1e26ecda7e000029" target="_blank">Am I safe to drive?</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/58f5c63f1e26ecda7e000029" target="_blank">Mexican Wave</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/58fdcc51b4f81a0b1e00003e" target="_blank">Pigs in a Pen</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/590300eb378a9282ba000095" target="_blank">Hungry Hippos</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/5904be220881cb68be00007d" target="_blank">Plenty of Fish in the Pond</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/590adadea658017d90000039" target="_blank">Fruit Machine</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/591eab1d192fe0435e000014" target="_blank">Car Park Escape</a></span>
