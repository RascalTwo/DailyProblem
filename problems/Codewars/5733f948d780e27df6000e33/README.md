[_metadata_:generated]: - "true"

# Training JS #34: methods of Math---pow() sqrt() and cbrt()

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5733f948d780e27df6000e33`](https://www.codewars.com/kata/5733f948d780e27df6000e33) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

In this lesson we learn three methods of Math: ```pow()``` ```sqrt()``` and ```cbrt()```. Their usage is very simple: ```sqrt()``` returns the square root of a number; ```cbrt()``` returns the cube root of a number; ```pow()``` returns the base to the exponent power.

Their definitions and detailed information:

- [Math.pow()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/pow)
- [Math.sqrt()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/sqrt)
- [Math.cbrt()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/cbrt)


Here we use some examples to understand their usage:

```javascript
var arr1=[1,4,9];
var sqroot=arr1.map(Math.sqrt);
console.log(sqroot);            //output: [1,2,3]

var arr2=[1,8,27];
var cbroot=arr2.map(Math.cbrt);
console.log(cbroot);            //output: [1,2,3]

var arr3=[1,2,3];
var pow2=arr3.map(x=>Math.pow(x,2));
var pow3=arr3.map(x=>Math.pow(x,3));
console.log(pow2);                  //output: [1,4,9]
console.log(pow3);                  //output: [1,8,27]
```
```pow()``` can use a simplified form: ```** operatorcan```. See example:
```javascript
var n=2
console.log(Math.pow(n,2));      //output: 4
console.log(n*n);                //output: 4
console.log(n**2);               //output: 4

console.log(Math.pow(n,3));      //output: 8
console.log(n*n*n);              //output: 8
console.log(n**3);               //output: 8
```
The second parameters of the ```pow()``` can be used as a fractional or decimal fraction, thus getting the same results as ```sqrt()``` and ```cbrt()```. See example:

```javascript
var n=64;
console.log(Math.sqrt(n));     //output: 8
console.log(Math.pow(n,0.5));  //output: 8
console.log(Math.pow(n,1/2));  //output: 8

console.log(Math.cbrt(n));                      //output: 3.9999999999999996
console.log(Math.pow(n,0.333333333333333333));  //output: 3.9999999999999996
console.log(Math.pow(n,1/3));                   //output: 3.9999999999999996
```
Look at the example above, what's the problem? Yes, the cube root of 64 should be 4, but we have not seen the 4, but see 3.9999999999999996. Due to the numerical precision of JS, the error will be produced in the calculation. This is a problem that can't be avoided. We should pay attention to this problem in use, look at the following example:
```javascript
function isCube(m,n){
  return Math.cbrt(m)==n;
}
console.log(isCube(27,3))               //output: true
console.log(isCube(64,4))               //output: false
console.log(isCube(125,5))               //output: false
```
This function is used to verify whether n is the cube root of m. It is obvious that the result is wrong. We should verify like this:
```javascript
function isCube(m,n){
  return m==n**3;
  //or: return m==n*n*n
}
console.log(isCube(27,3))               //output: true
console.log(isCube(64,4))               //output: true
console.log(isCube(125,5))              //output: true
```
This method can also be used to verify the number of squares.
The following three methods are used to verify that the square root of a number is an integer:
```javascript
function intRoot1(n){
  return Number.isInteger(Math.sqrt(n));
}
function intRoot2(n){
  return Math.sqrt(n)%1==0;
}
function intRoot3(n){
  var x=Math.round(Math.sqrt(n));
  return x*x==n;
}

console.log(intRoot1(16))               //output: true
console.log(intRoot2(16))               //output: true
console.log(intRoot3(16))               //output: true
```
The third method is the longest, but it is the most stable one.

Ok, lesson is over. let's us do some task.

## Task

Coding in function ```cutCube```. function accept 2 parameter: ```volume``` and ```n```. ```volume``` is the volume of a cube. If we cut the cube into ```n``` block. please determine whether the length of the cube is an integer. return true or false. 

For exmaple: 

volume=27, it can be divided into 27 blocks, each small cube side length is 1
```
cutCube(27,27) should return true
```
volume=512, it can be divided into 8 blocks, each small cube side length is 4
```
cutCube(512,8) should return true
```
volume=512, it can be divided into 64 blocks, each small cube side length is 2
```
cutCube(512,64) should return true
```
If the side length of small cube is not a integer, should return false.
```
cutCube(256,8) should return false
cutCube(27,3) should return false
cutCube(123,456) should return false
```
If it can't be divided evenly into ```n``` small cubes, should return false too.
```
cutCube(50000,50) should return false
cutCube(256,4) should return false
```
The two examples above seems to meet our requirements, but please note: a cube is unable to evenly divided into 50 pieces or 4 pieces. Only cubic numbers(such as 8,27,64,125,216...) can be used to divide the cube evenly.

    
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
 
