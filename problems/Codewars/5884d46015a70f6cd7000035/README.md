[_metadata_:generated]: - "true"

# Playing with Sets : Intersection

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5884d46015a70f6cd7000035`](https://www.codewars.com/kata/5884d46015a70f6cd7000035) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

[Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) objects are new JavaScript built-in objects defined since [ECMAScript 2015](http://www.ecma-international.org/ecma-262/6.0/#sec-set-objects.)

A **Set** lets you store unique values of any type. It comes with some useful methods like `.add`, `.clear`, `.has` . . . **BUT** some "Set operations" are missing, like . . . 

# Intersection

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Venn0001.svg/330px-Venn0001.svg.png" style="max-width:200px">

A new set can be constructed by determining which members two sets have "in common". The **intersection** of A and B, denoted by A ∩ B, is the set of all things that are members of both A and B. If A ∩ B = ∅, then A and B are said to be **disjoint**.

### Examples:
```
  {1, 2} ∩ {1, 2} = {1, 2}.
  {1, 2} ∩ {2, 3} = {2}.
```
# Task

Create function `inter` getting 2 sets as arguments and returning a **new Set** as result of intersection of these 2 sets.
### Examples:
```javascript
A = new Set([1,2]);
B = new Set([2,3]);

C = inter(A,B) // -> {2}
```

&nbsp;

" May the Code be with you ! "
<img src="https://en.wikipedia.org/w/extensions/wikihiero/img/hiero_E20.png" align="right" title="There's more than ONE Set!">
