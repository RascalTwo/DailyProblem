[_metadata_:generated]: - "true"

# Fun with ES6 Classes #3 - Cuboids, Cubes and Getters

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`56fbdda707cff41b68000de2`](https://www.codewars.com/kata/56fbdda707cff41b68000de2) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Fun with ES6 Classes #3 - Cuboids, Cubes and Getters

## Task

Define the following classes.

### I. Cuboid

The object ```constructor``` for the ```class Cuboid``` should receive exactly three arguments in the following order: ```length, width, height``` and store these three values in ```this.length```, ```this.width``` and ```this.height``` respectively.

The ```class Cuboid``` should then have a **getter** ```surfaceArea``` which returns the surface area of the cuboid and a getter ```volume``` which returns the volume of the cuboid.

### II. Cube

```class Cube``` is a subclass of ```class Cuboid```.  The ```constructor``` function of ```Cube``` should receive one argument only, its ```length```, and use that value passed in to set ```this.length```, ```this.width``` and ```this.height```.

*Hint: Make a call to ```super```, passing in the correct arguments, to make life easier ;)*

## Related Articles

Listed below are a few articles of interest that may help you complete this Kata:

1. [Stack Overflow - What are getters and setters in ES6?](http://stackoverflow.com/questions/28222276/what-are-getters-and-setters-for-in-ecmascript-6-classes)
2. [getter - Javascript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
