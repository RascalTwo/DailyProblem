[_metadata_:generated]: - "true"

# Coding 3min : Remove screws I

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                                                                                                                                                       |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5710a50d336aed828100055a`](https://www.codewars.com/kata/5710a50d336aed828100055a) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924063/c_bnvpsm.svg" alt="C#" title="C#" width="50" />](solve.cs)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

John is a worker, his job is to remove screws from a machine. There are 2 types of screws: slotted (`-`) and cross (`+`). John has two screwdrivers, one for each type of screw.

The input will be a (non-empty) string of screws, e.g. : `"---+++"`

When John begins to work, he stands at the first screw, with the correct screwdriver in his hand, and another in his tool kit. He works from left to right, removing every screw. When necessary, he switches between the screwdriver in his hand and the one in his tool kit.

Each action takes a set amount of time:
* remove one screw :               1 second
* move to the next screw:          1 second
* switch screwdrivers:             5 seconds

Your task is to return the total time taken to remove all the screws, in seconds.


## Examples

In order to be more clear, we use `ABCDEF` to represent the screws. The number in brackets is the time in seconds:

```
screws: "---+++"
         ABCDEF

remove A (1) + move to B (1) + remove B (1) + 
move to C (1) + remove C (1) + move to D (1) +
switch screwdriver (5) + remove D (1) +
move to E (1) + remove E (1) + move to F (1) + remove F (1)

total time = 16 seconds

```

Another example:
```
screws: "-+-+-+"
         ABCDEF

remove A (1) +
move to B (1) + switch screwdriver (5) + remove B (1) +
move to C (1) + switch screwdriver (5) + remove C (1) +
move to D (1) + switch screwdriver (5) + remove D (1) +
move to E (1) + switch screwdriver (5) + remove E (1) +
move to F (1) + switch screwdriver (5) + remove F (1)

total time = 36 seconds 
```


## Variations

* [Golf version](http://www.codewars.com/kata/57109bf197b4b3853a000274)

* This work method may not be the fastest. For a better method, see [Remove screws II](http://www.codewars.com/kata/5710a8fd336aed00d9000594)


### Series:
 - [Bug in Apple](http://www.codewars.com/kata/56fe97b3cc08ca00e4000dc9)
 - [Father and Son](http://www.codewars.com/kata/56fe9a0c11086cd842000008)
 - [Jumping Dutch act](http://www.codewars.com/kata/570bcd9715944a2c8e000009)
 - [Planting Trees](http://www.codewars.com/kata/5710443187a36a9cee0005a1)
 - [Give me the equation](http://www.codewars.com/kata/56fe9b65cc08cafbc5000de3)
 - [Find the murderer](http://www.codewars.com/kata/570f3fc5b29c702c5500043e)
 - [Reading a Book](http://www.codewars.com/kata/570ca6a520c69f39dd0016d4)
 - [Eat watermelon](http://www.codewars.com/kata/570df12ce6e9282a7d000947)
 - [Special factor](http://www.codewars.com/kata/570e5d0b93214b1a950015b1)
 - [Guess the Hat](http://www.codewars.com/kata/570ef7a834e61306da00035b)
 - [Symmetric Sort](http://www.codewars.com/kata/5705aeb041e5befba20010ba)
 - [Are they symmetrical?](http://www.codewars.com/kata/5705cc3161944b10fd0004ba)
 - [Max Value](http://www.codewars.com/kata/570771871df89cf59b000742)
 - [Trypophobia](http://www.codewars.com/kata/56fe9ffbc25bf33fff000f7c)
 - [Virus in Apple](http://www.codewars.com/kata/5700af83d1acef83fd000048)
 - [Balance Attraction](http://www.codewars.com/kata/57033601e55d30d3e0000633)
 - [Remove screws I](http://www.codewars.com/kata/5710a50d336aed828100055a)
 - [Remove screws II](http://www.codewars.com/kata/5710a8fd336aed00d9000594)
 - [Regular expression compression](http://www.codewars.com/kata/570bae4b0237999e940016e9)
 - [Collatz Array(Split or merge)](http://www.codewars.com/kata/56fe9d579b7bb6b027000001)
 - [Tidy up the room](http://www.codewars.com/kata/5703ace6e55d30d3e0001029)
 - [Waiting for a Bus](http://www.codewars.com/kata/57070eff924f343280000015)
