[_metadata_:generated]: - "true"

# Blood-Alcohol Content

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`571b6a4a7beb0a8ade0007a8`](https://www.codewars.com/kata/571b6a4a7beb0a8ade0007a8) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Bob drinks too much, and he gets in trouble for it a lot. He drinks so much, in fact, that he has broken the local law enforcement's breathalizer with his alcoholic breath! Bob feels simply aweful, so he wants to make up for it by creating a function that will calculate his blood-alcohol level for them. Unfortunately, Bob has gotten too inebriated to do any programming today, so he needs your help!

He did manage to research the formula for blood-alcohol content before getting too drunk, which he describes below.

BAC calculator Formula:

    BAC% = (A × 5.14 / W × r) - .015 × H 

    A: Total alcohol consumed, in ounces (oz)
    W: Body weight, in pounds (lbs)
    r: The alcohol distribution ratio, 0.73 for man, and 0.66 for women
    H: Time passed since drinking, in hours

Source: 

http://www.endmemo.com/medical/bac.php

Alcohol consumed will be passed as a ```drinks``` object with two properties: ```ounces``` (the total volume of beverage consumed in ounces), and ```abv``` (the % of alcohol by volume of the beverage as a floating point number--such as __0.05__ for 5% abv beer or __0.4__ for 40% abv whisky). For simplicity, Bob assures us that he drinks the same kind of beverage each time he drinks.

The gender will be passed as a string, either __"male"__ or __"female"__.

<span style="font-size:1.12em">Output must be returned as a __number__ data-type</span>, greater than or equal to 0, with up to 4 decimal places. No error handling will be required.

Using these parameters, create the function that will calculate Bob's and other partier's BAC.
