[_metadata_:generated]: - "true"

# Training JS #29: methods of arrayObject---concat() and join()

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5731861d05d14d6f50000626`](https://www.codewars.com/kata/5731861d05d14d6f50000626) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

This lesson we learn two methods of array: ```concat()``` and ```join()```. We have seen ```concat()``` in the stringObject method, but the method of the arrayObject  is different from the stringObject method, so we need to learn again. When studying the stringObject method ```split()```, we have simply learned the ```join()``` method.  This time we will review and explain it in detail.

Their definitions and syntax please refer to: 

- [Array.prototype.concat()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)
- [Array.prototype.join()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)

(Please forgive me for my laziness;-)

Here are some examples to help us understand the use of ```concat()``` and ```join()```:

We first learn the ```concat()``` method, which can add some elements to the end of the array. ```concat()``` can have more and more parameters, and the parameter can be values, array or otherthings. Look this example:
```javascript
var arr1=[1,2,3],arr2=[4,5,6];
//The following ways can achieve the same purpose:
//It can use an array as parameter
console.log(arr1.concat(arr2));
//also can use some values as parameters
console.log(arr1.concat(4,5,6));
//also can use more than one array as parameters
console.log(arr1.concat([4],[5],[6]));
//use ... accept the value of an enumeration
console.log(arr1.concat(...arr2));
//It can be used continuously
console.log(arr1.concat(4).concat(5).concat(6)); 
//output:
[ 1, 2, 3, 4, 5, 6 ]
[ 1, 2, 3, 4, 5, 6 ]
[ 1, 2, 3, 4, 5, 6 ]
[ 1, 2, 3, 4, 5, 6 ]
[ 1, 2, 3, 4, 5, 6 ]
```
```concat()``` can be used for the flat output of two-dimensional or multidimensional arrays. look this example:
```javascript
var arr=[[1,2],[3,4],[5,6]];
var result=[];
for (var i=0;i<arr.length;i++) 
  result=result.concat(arr[i]);
console.log(result);    //output: [ 1, 2, 3, 4, 5, 6 ]
```
This example by traversing the array and ```concat()``` method to get a one-dimensional array, which contains all the elements of the two-dimensional array. Or use more simple code:
```javascript
var arr=[[1,2],[3,4],[5,6]];
var result=[].concat(...arr);
console.log(result);    //output: [ 1, 2, 3, 4, 5, 6 ]
```
```...arr``` takes all the elements of arr (some one-dimensional array) as parameters of ```concat()```.

Here we look at some examples of ```join()```. Its main purpose is to merge the elements of an array into a string, using a parameter ```separator``` to connect each element. If the ```separator``` is omitted, the default separator is ```","```:

```javascript
var arr=[1,2,3,4,5];
console.log(arr.join());      //output: 1,2,3,4,5
console.log(arr.join(","));   //output: 1,2,3,4,5
console.log(arr.join(" "));   //output: 1 2 3 4 5
console.log(arr.join("and")); //output: 1and2and3and4and5
```
One of its classic applications is to produce a specified number of repeating characters:
```javascript
function repeat(s,n){
  return [...Array(n+1)].join(s);
}
console.log(repeat("a",5)); //output: aaaaa
console.log(repeat("abc",5)); //output: abcabcabcabcabc
```
It is also a good choice to connect multiple strings. When there is a large number of strings that need to be connected to a string, the use of the + operator speed is slow, the correct method should be to put them into the array, and then use the ```join()``` method:
```javascript
//use + operator:
var result="";
for (var i=0;i<26;i++) 
  result+=String.fromCharCode(97+i);
console.log(result)   //output: abcdefghijklmnopqrstuvwxyz
//use join() method:
var cache=[];
for (var i=0;i<26;i++) cache[i]=String.fromCharCode(97+i);
var result=cache.join("");
console.log(result)   //output: abcdefghijklmnopqrstuvwxyz
```
Of course, when the amount of data is very small, we do not feel the difference in speed.

Ok, lesson is over. let's us do some task.

## Task

Coding in function ```bigToSmall```. function accept 1 parameter ```arr```(2D number array). 

Your task is: First to all, refer to the example above, flat output ```arr``` to a one-dimensional array.

And then sort array in descending order.

Finally, use the separator ">" to connect the elements into a string. 

Don't complain about the situation like ```1>1``` is not reasonable, it is just a separator.

Some example:
```
bigToSmall([[1,2],[3,4],[5,6]]) should return "6>5>4>3>2>1"
bigToSmall([[1,3,5],[2,4,6]]) should return "6>5>4>3>2>1"
bigToSmall([[1,1],[1],[1,1]]) should return "1>1>1>1>1"
```
   
    
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
 
