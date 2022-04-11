[_metadata_:generated]: - "true"

# Find the vowels

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5680781b6b7c2be860000036`](https://www.codewars.com/kata/5680781b6b7c2be860000036) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

We want to know the index of the vowels in a given word, for example, there are two vowels in the word super (the second and fourth letters). 

So given a string "super", we should return a list of `[2, 4]`.

	Some examples:
	Mmmm  => []
	Super => [2,4]
	Apple => [1,5]
	YoMama -> [1,2,4,6]

### NOTES

* Vowels in this context refers to: a e i o u y (including upper case)
* This is indexed from `[1..n]` (not zero indexed!)

