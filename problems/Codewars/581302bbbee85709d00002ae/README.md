[_metadata_:generated]: - "true"

# Halloween: trick or treat!

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`581302bbbee85709d00002ae`](https://www.codewars.com/kata/581302bbbee85709d00002ae) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

>When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own, to enjoy the process  --myjinxin2015 said

# Description:
 
 Halloween is coming, and many children are in front of your house. They are shouting: "trick or treat!" So you need to give them some candy, let them leave. 
 
 - Arguments:
 
   - `children`:  numbers of children, more than or equals to 2
 
   - `candies`:  packets of items, like this: 
 
 ```
 [["candy","apple","candy"],["candy","candy"],["candy","candy"]]
 ```
 
 - Results: 
   - If the children get what they want, return "Thank you, strange uncle!"
   - If not, return "Trick or treat!"
   
 - How to let the children satisfied? 
   - 1 - Each child has at least **two** candies;
   - 2 - Each child gets the **same amount** of candy.
   - 3 - No children get the **"bomb"** ;-)
   - 4 - Packets cannot be divided, each child gets a full packet
   
# Some Examples

```
trickOrTreat(3,[["candy","apple","candy"],["candy","candy"],["candy","candy"]])
should return: "Thank you, strange uncle!"(Don't mind apple)

trickOrTreat(3,[["candy","apple"],["apple","candy"],["candy","apple"]])
should return: "Trick or treat!"(Each child has only got 1 candy)

trickOrTreat(3,[["candy","apple","candy"],["candy","candy"],["candy","candy","candy"]])
should return: "Trick or treat!"(The amount of candy are diffrent)

trickOrTreat(3,[["candy","apple","candy"],["candy","candy"]])
should return: "Trick or treat!"(One child has no candy)

trickOrTreat(3,[["candy","apple","candy"],["candy","candy"],["candy","bomb","candy"]])
should return: "Trick or treat!"(Some child got a bomb)
```
You can assume that the arguments are valid arrays (like the examples above, no empty array).
