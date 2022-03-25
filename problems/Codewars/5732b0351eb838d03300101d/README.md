[_metadata_:generated]: - "true"

# Training JS #31: methods of arrayObject---isArray() indexOf() and toString()

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5732b0351eb838d03300101d`](https://www.codewars.com/kata/5732b0351eb838d03300101d) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

This lesson we learn the last three methods: ```isArray()``` ```indexOf()``` and ```toString()```. Each of these three methods have their own purpose and put them together just because this is the last lesson of arrayObject ;-)

For more information, please refer to: 

- [Array.prototype.isArray()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray)
- [Array.prototype.indexOf()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf) 
- [Array.prototype.toString()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toString) 

Here are some examples to help us understand the use of ```isArray()```  ```indexOf``` and ```toString()```:

```isarray()``` is a static method, its main-body can only be ```Array```. it returns a Boolean value, which means that the parameter is an array or not. See example:
```javascript
var a=[1], b=1, c="1", d={1:1}, e=true;
console.log(Array.isArray(a)); //true    a is an array
console.log(Array.isArray(b)); //false   b is not an array
console.log(Array.isArray(c)); //false   c is not an array
console.log(Array.isArray(d)); //false   d is not an array
console.log(Array.isArray(e)); //false   e is not an array
```
It is often used to check the validity of the parameters. There are many other ways to determine the parameter type, and we will learn from the next lesson.

We have seen ```indexOf()``` used for stringObject. The array object can also be used. its Usage is basically the same as the string object.

It's usually used to determine whether an array contains an element or not. Its return value is the index of element. If there is no such element in the array, return -1. See example:
```javascript
var arr=[1,2,3,4,5];
console.log(arr.indexOf(1));             //output: 0  arr[0]=1
console.log(arr.indexOf(5));             //output: 4  arr[4]=5
console.log(arr.indexOf(6));             //output: -1 no 6 in the array
```

More examples please refer to [#17: Methods of String object--indexOf(), lastIndexOf() and search()](http://www.codewars.com/kata/57277a31e5e51450a4000010)

All objects in JS have ```toString()``` methods. Its function is to return a string representation of an object. Converting an object into a string, ```toString()``` is not the easiest way to do it. A lot of ways to do this: 
```javascript
var arr=[1,2,3,4,5];
console.log(arr.toString()); //1,2,3,4,5
console.log(arr+"");         //1,2,3,4,5
console.log(arr.join());     //1,2,3,4,5
```
Sometimes the performance of ```toString()```' is not satisfactory, ```JSON.stringify()``` provides us with a more powerful feature:
```javascript
var arr1=["1","2","3","4","5"];
console.log(arr1.toString());       //1,2,3,4,5
console.log(JSON.stringify(arr1));  //["1","2","3","4","5"]

var arr2=[[1,2],[3,4],[5]];
console.log(arr2.toString());       //1,2,3,4,5
console.log(JSON.stringify(arr2));  //[[1,2],[3,4],[5]]
```

Ok, lesson is over. let's us do some task.

## Task

Coding in function ```blackAndWhite```. function accept 1 parameter ```arr```(a number array). 
    
If ```arr``` is not an array, function should return:
```
"It's a fake array"
```
If ```arr``` contains elements 5 and 13, function should return:
```
"It's a black array"
```

If `arr` contains neither 5 nor 13, function should return:
```
"It's a white array"
```
   

## Examples

```
blackAndWhite(5,13) should return "It's a fake array"
blackAndWhite([5,13]) should return "It's a black array"
blackAndWhite([5,12]) should return "It's a white array" 
```

Using ```string template``` and ```ternary operator``` can make your work easier.

## [Series](http://github.com/myjinxin2015/Katas-list-of-Training-JS-series)

( ↑↑↑ Click the link above can get my newest kata list, Please add it to your favorites)

 - [#1: create your first JS function helloWorld](http://www.codewars.com/kata/571ec274b1c8d4a61c0000c8)
 - [#2: Basic data types--Number](http://www.codewars.com/kata/571edd157e8954bab500032d)
 - [#3:  Basic data types--String](http://www.codewars.com/kata/571edea4b625edcb51000d8e)
 - [#4:  Basic data types--Array](http://www.codewars.com/kata/571effabb625ed9b0600107a)
 - [#5:  Basic data types--Object](http://www.codewars.com/kata/571f1eb77e8954a812000837)
 - [#6:  Basic data types--Boolean and conditional statements if..else](http://www.codewars.com/kata/571f832f07363d295d001ba8)
 - [#7:  if..else and ternary operator](http://www.codewars.com/kata/57202aefe8d6c514300001fd)
 - [#8: Conditional statement--switch](http://www.codewars.com/kata/572059afc2f4612825000d8a)
 - [#9: loop statement --while and do..while](http://www.codewars.com/kata/57216d4bcdd71175d6000560)
 - [#10: loop statement --for](http://www.codewars.com/kata/5721a78c283129e416000999)
 - [#11: loop statement --break,continue](http://www.codewars.com/kata/5721c189cdd71194c1000b9b)
 - [#12: loop statement --for..in and for..of](http://www.codewars.com/kata/5722b3f0bd5583cf44001000)
 - [#13: Number object and  its properties](http://www.codewars.com/kata/5722fd3ab7162a3a4500031f)
 - [#14: Methods of Number object--toString() and toLocaleString()](http://www.codewars.com/kata/57238ceaef9008adc7000603)
 - [#15: Methods of Number object--toFixed(), toExponential() and toPrecision()](http://www.codewars.com/kata/57256064856584bc47000611)
 - [#16: Methods of String object--slice(), substring() and substr()](http://www.codewars.com/kata/57274562c8dcebe77e001012)
 - [#17: Methods of String object--indexOf(), lastIndexOf() and search()](http://www.codewars.com/kata/57277a31e5e51450a4000010)
 - [#18: Methods of String object--concat() split() and its good friend join()](http://www.codewars.com/kata/57280481e8118511f7000ffa)
 - [#19: Methods of String object--toUpperCase() toLowerCase() and replace()](http://www.codewars.com/kata/5728203b7fc662a4c4000ef3)
 - [#20: Methods of String object--charAt() charCodeAt() and fromCharCode()](http://www.codewars.com/kata/57284d23e81185ae6200162a)
 - [#21: Methods of String object--trim() and the string template](http://www.codewars.com/kata/5729b103dd8bac11a900119e)
 - [#22: Unlock new skills--Arrow function,spread operator and deconstruction](http://www.codewars.com/kata/572ab0cfa3af384df7000ff8)
 - [#23: methods of arrayObject---push(), pop(), shift() and unshift()](http://www.codewars.com/kata/572af273a3af3836660014a1)
 - [#24: methods of arrayObject---splice() and slice()](http://www.codewars.com/kata/572cb264362806af46000793)
 - [#25: methods of arrayObject---reverse() and sort()](http://www.codewars.com/kata/572df796914b5ba27c000c90)
 - [#26: methods of arrayObject---map()](http://www.codewars.com/kata/572fdeb4380bb703fc00002c)
 - [#27: methods of arrayObject---filter()](http://www.codewars.com/kata/573023c81add650b84000429)
 - [#28: methods of arrayObject---every() and some()](http://www.codewars.com/kata/57308546bd9f0987c2000d07)
 - [#29: methods of arrayObject---concat() and join()](http://www.codewars.com/kata/5731861d05d14d6f50000626)
 - [#30: methods of arrayObject---reduce() and reduceRight()](http://www.codewars.com/kata/573156709a231dcec9000ee8)
 - [#31: methods of arrayObject---isArray() indexOf() and toString()](http://www.codewars.com/kata/5732b0351eb838d03300101d)
 - [#32: methods of Math---round() ceil() and floor()](http://www.codewars.com/kata/5732d3c9791aafb0e4001236)
 - [#33: methods of Math---max() min() and abs()](http://www.codewars.com/kata/5733d6c2d780e20173000baa)
 - [#34: methods of Math---pow() sqrt() and cbrt()](http://www.codewars.com/kata/5733f948d780e27df6000e33)
 - [#35: methods of Math---log() and its family](http://www.codewars.com/kata/57353de879ccaeb9f8000564)
 - [#36: methods of Math---kata author's lover:random()](http://www.codewars.com/kata/5735956413c2054a680009ec)
 - [#37: Unlock new weapon---RegExp Object](http://www.codewars.com/kata/5735e39313c205fe39001173)
 - [#38: Regular Expression--"^","$", "." and test()](http://www.codewars.com/kata/573975d3ac3eec695b0013e0)
 - [#39: Regular Expression--"?", "*", "+" and "{}"](http://www.codewars.com/kata/573bca07dffc1aa693000139)
 - [#40: Regular Expression--"|", "[]" and "()"](http://www.codewars.com/kata/573d11c48b97c0ad970002d4)
 - [#41: Regular Expression--"\"](http://www.codewars.com/kata/573e6831e3201f6a9b000971)
 - [#42: Regular Expression--(?:), (?=) and (?!)](http://www.codewars.com/kata/573fb9223f9793e485000453)
 
