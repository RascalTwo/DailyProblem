[_metadata_:generated]: - "true"

# Magic The Gathering #2: Mana

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`567b22d9ba0e6b8c2400001e`](https://www.codewars.com/kata/567b22d9ba0e6b8c2400001e) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Magic The Gathering is a collectible card game that features wizards battling against each other with spells and creature summons. The game itself can be quite complicated to learn. In this series of katas, we'll be solving some of the situations that arise during gameplay. You won't need any prior knowledge of the game to solve these contrived problems, as I will provide you with enough information.

In Magic, each spell you cast has a cost associated with it. Those costs are represented like so:

````
"B" -> One black mana
"G" -> One green mana
"R" -> One red mana
"U" -> One blue mana
"W" -> One white mana
"1" -> One colorless mana
"2" -> Two colorless mana
"3BBG" -> Three colorless mana, two black mana, one green mana
````

Your mana pool will be one string that contains all of your available mana like so:
````
"10WWWRRRRR" -> Means you have 10 colorless mana, 3 white mana and 5 red mana to work with.
````
The caveat is, any left over colored mana, can be used as colorless mana. So if you have a spell that costs "1B" and your mana pool has "UB" you can cast that spell, since the "U" can be used as a colorless mana.

With this knowlege, write a function canCast() that takes in a string for your mana pool and then any number of spells' casting costs. Return true if you have enough mana to cast the spell, false otherwise.

Examples:
````javascript
canCast("BBRR","BR") -> true
canCast("BBRR","BR","BR") -> true
canCast("4R","3R") -> true
canCast("2", "R") -> false
canCast("RR", "2") -> true
````
````coffeescript
canCast("BBRR","BR") # true
canCast("BBRR","BR","BR") # true
canCast("4R","3R") # true
canCast("2", "R") # false
canCast("RR", "2") # true
````

<div style="width: 320px; text-align: center; color: white; border: white 1px solid;">
Check out my other Magic The Gathering katas:
</div>
<div>
<a style='text-decoration:none' href='http://www.codewars.com/kata/magic-the-gathering-number-1-creatures'><span style='color:#00C5CD'>Magic The Gathering #1:</span> Creatures</a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/magic-the-gathering-number-2-mana'><span style='color:#00C5CD'>Magic The Gathering #2:</span> Mana</a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/magic-the-gathering-number-3-spell-stack'><span style='color:#00C5CD'>Magic The Gathering #3:</span> Spell Stack</a><br />

</div>

