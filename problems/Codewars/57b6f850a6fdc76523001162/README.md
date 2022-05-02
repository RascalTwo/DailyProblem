[_metadata_:generated]: - "true"

# Hit Count

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`57b6f850a6fdc76523001162`](https://www.codewars.com/kata/57b6f850a6fdc76523001162) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Introduction

You are the developer working on a website which features a large counter on its homepage, proudly displaying the number of happy customers who have downloaded your companies software.

You have been tasked with adding an effect to this counter to make it more interesting.  

Instead of just displaying the count value immediatley when the page loads, we want to create the effect of each digit cycling through its preceding numbers before stopping on the actual value.

<img src="http://www.customerexperienceinsight.com/wp-content/uploads/2013/05/96102264.jpg" style="width: 350px;height: 100px"></img>


# Task

As a step towards achieving this; you have decided to create a function that will produce a multi-dimensional array out of the hit count value.  Each inner dimension of the array represents an individual digit in the hit count, and will include all numbers that come before it, going back to 0.

## Rules
* The function will take one argument which will be a four character `string` representing hit count
* The function must return a multi-dimensional array containing four inner arrays
* The final value in each inner array must be the actual value to be displayed
* Values returned in the array must be of the type `number`

**Examples**

```javascript
counterEffect("1250") // [[0,1],[0,1,2],[0,1,2,3,4,5],[0]] 
counterEffect("0050") // [[0],[0],[0,1,2,3,4,5],[0]] 
counterEffect("0000") // [[0],[0],[0],[0]]
```

```php
counter_effect("1250") // [[0,1],[0,1,2],[0,1,2,3,4,5],[0]]
counter_effect("0050") // [[0],[0],[0,1,2,3,4,5],[0]]
counter_effect("0000") // [[0],[0],[0],[0]]
```