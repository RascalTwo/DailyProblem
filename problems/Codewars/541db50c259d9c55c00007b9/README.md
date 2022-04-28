[_metadata_:generated]: - "true"

# Node.js Intro

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`541db50c259d9c55c00007b9`](https://www.codewars.com/kata/541db50c259d9c55c00007b9) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

JavaScript (and CoffeeScript by extension) is a language that is heavily dependent on a **run-time environment**.  While most people learn JS in a *browser* environment, there are [other environemnts that run outside of a browser](https://en.wikipedia.org/wiki/JavaScript#Uses_outside_web_pages).  Codewars runs your code in a *[Node.js](http://nodejs.org/)* environment.

This kata is an attempt to introduce the NodeJS environment.

Environment Differences
----

The runtime environment gives your code the ability to interact with software outside of the language itself.  For example, a browser environment has several built-ins that let you interact with a webpage.  You can use functions like `getElementById` or `XMLHttpRequest`.

[Node.js](http://nodejs.org/), however, cannot use those browser-specific built-ins (go ahead, try).  Node.js is an environment for javascript that is meant to run on your computer (server-side).  So while you lose the ability to work with browser built-ins, you gain access to NodeJS-specific code.

Kata
-----

We are going to replicate the kata [Base64 Encoding](http://www.codewars.com/kata/base64-encoding/javascript), but instead of creating our own encoding / decoding functions, we will use [NodeJS' Buffer module](http://nodejs.org/api/buffer.html) to do it for us.

Create the function `String.prototype.toBase64` that encodes a string in Base64.  Also create the function `String.prototype.fromBase64` that decodes a Base64 string into `utf8`.

Examples
----
```javascript
// should return 'dGhpcyBpcyBhIHN0cmluZyEh'
'this is a string!!'.toBase64(); 

// should return 'this is a string!!'
'dGhpcyBpcyBhIHN0cmluZyEh'.fromBase64();
```
```coffeescript
# should return 'dGhpcyBpcyBhIHN0cmluZyEh'
"this is a string!!".toBase64()

# should return 'this is a string!!'
"dGhpcyBpcyBhIHN0cmluZyEh".fromBase64()
```
    
Tips
----

To use a NodeJS module, you need to `require` it into your code.  For example, if I wanted to use the `util` module, I could write
```javascript
//require the 'util' module into your code
var util = require('util')
console.log(util.isRegExp(/hi/)) 
```
```coffeescript
util = require "util"
console.log util.isRegExp /hi/
```
The NodeJS built-in function `require` knows exactly how to find the module, so no extra work is needed.  After you have `require`d a module into your code, you can use any of the methods / properties for it.

The [NodeJS documentation](http://nodejs.org/api/) is helpful, so I suggest you look at that.  If you plan on working with NodeJS at all in the future, it is beneficial to know what features it has built-in.
