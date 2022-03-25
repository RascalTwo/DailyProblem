[_metadata_:generated]: - "true"

# 80's Kids #1: How Many Licks Does it Take?

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`566091b73e119a073100003a`](https://www.codewars.com/kata/566091b73e119a073100003a) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

How many licks does it take to get to the tootsie roll center of a tootsie pop?

A group of engineering students from Purdue University reported that its licking machine, modeled after a human tongue, took an average of 364 licks to get to the center of a Tootsie Pop. Twenty of the group's volunteers assumed the licking challenge-unassisted by machinery-and averaged 252 licks each to the center.

Your task, if you choose to accept it, is to write a function that will return the number of licks it took to get to the tootsie roll center of a tootsie pop, given some environmental variables.

Everyone knows it's harder to lick a tootsie pop in cold weather but it's easier if the sun is out. You will be given an object of environmental conditions for each trial paired with a value that will increase or decrease the number of licks. The environmental conditions all apply to the same trial.

Assuming that it would normally take 252 licks to get to the tootsie roll center of a tootsie pop, return the new total of licks along with the condition that proved to be most challenging (causing the most added licks) in that trial.

Example:
```
totalLicks({ "freezing temps": 10, "clear skies": -2 });
```
Should return:
```
"It took 260 licks to get to the tootsie roll center of a tootsie pop. The toughest challenge was freezing temps."
```
Other cases:
If there are no challenges, the toughest challenge sentence should be omitted. If there are multiple challenges with the highest toughest amount, the first one presented will be the toughest.
If an environment variable is present, it will be either a positive or negative integer. No need to validate.

<div style="width: 320px; text-align: center; color: white; border: white 1px solid;">
Check out my other 80's Kids Katas:
</div>
<div>
<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-1-how-many-licks-does-it-take'><span style='color:#00C5CD'>80's Kids #1:</span> How Many Licks Does It Take</a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-2-help-alf-find-his-spaceship'><span style='color:#00C5CD'>80's Kids #2:</span> Help Alf Find His Spaceship</a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-3-punky-brewsters-socks'><span style='color:#00C5CD'>80's Kids #3:</span> Punky Brewster's Socks</a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-4-legends-of-the-hidden-temple'><span style='color:#00C5CD'>80's Kids #4:</span> Legends of the Hidden Temple</a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-5-you-cant-do-that-on-television'><span style='color:#00C5CD'>80's Kids #5:</span> You Can't Do That on Television</a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-6-rock-em-sock-em-robots'><span style='color:#00C5CD'>80's Kids #6:</span> Rock 'Em, Sock 'Em Robots</a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-7-shes-a-small-wonder'><span style='color:#00C5CD'>80's Kids #7:</span> She's a Small Wonder</a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-8-the-secret-world-of-alex-mack'><span style='color:#00C5CD'>80's Kids #8:</span> The Secret World of Alex Mack</a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-9-down-in-fraggle-rock'><span style='color:#00C5CD'>80's Kids #9:</span> Down in Fraggle Rock </a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-10-captain-planet'><span style='color:#00C5CD'>80's Kids #10:</span> Captain Planet </a><br />


</div>

