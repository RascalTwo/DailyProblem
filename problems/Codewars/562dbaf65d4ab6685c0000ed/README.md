[_metadata_:generated]: - "true"

# Lorraine Wants to Win the TV Contest

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`562dbaf65d4ab6685c0000ed`](https://www.codewars.com/kata/562dbaf65d4ab6685c0000ed) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

There are many word games that can help to make our minds more agile.
Many TV programs, in different countries, use them as entertainment for the audience.

Lorraine had tried to win one of them many times but she was not successful in her attempts. The TV contest is as follows:

- The TV show host gives a random caller a scrambled word (that is incomprehensible) and by rearranging those letters they have to discover a word that is in the Oxford English Dictionary.


- They have only 25 seconds to discover the word.

Her friend Bruce obtained the list of 2000, frequently used, English words used by the TV show.

Help Lorraine by making a function that will give her a list of all valid words that may be obtained by rearranging the scrambled word.
There always be at least one valid word for each test case.

Let's see some test cases:
```python 
unscramble("shi") == ['his']

unscramble("nowk") == ['know']

unscramble("amle") == ['male', 'meal']
```
The list of words that Bruce obtained (keep the secret!) is named ```word_list```, in ruby ```$word_list``` and javascript ```wordList```.
For words with more than six letters we have a challenge with speed.
Try to create a suitable memoized data structure for fast hashing using the provided ```word_list```.

Remember that all the words will correspond to U.K. English (Oxford Dictionary).
