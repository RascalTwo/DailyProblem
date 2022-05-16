[_metadata_:generated]: - "true"

# Node.js Async I/O

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`542106e2dda52658bf00001a`](https://www.codewars.com/kata/542106e2dda52658bf00001a) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

###Description

If you have completed my previous katas [Intro to NodeJS](http://www.codewars.com/kata/541db50c259d9c55c00007b9) and [Password Hashes](http://www.codewars.com/kata/54207f9677730acd490000d1), you should know the gist of [requiring node modules](http://nodejs.org/api/modules.html#modules_modules) into your code.  If you are new to NodeJS and haven't completed the previous katas, I recommend you do so.

As it turns out, unless you are coding something really processor intensive, the slowest parts of nearly any program is [I/O](http://en.wikipedia.org/wiki/Input/output).  One of NodeJS' key features is the ability to [asynchronously deal with I/O](http://en.wikipedia.org/wiki/Asynchronous_I/O), and is thus the focus of this kata.

----

###Kata Specifications

To practice NodeJS Async conventions, we will create the function `execute` that asynchronously runs a Bash `command` to Codewars' linux environment (think command-line Windows users).

The `execute` function takes 2 parameters: a `command` string and a `callback` function.  Your function should essentially begin the `command`, and whenever the command is complete, run the `callback` function.

To actually run a command, you will need to read about the [Child Process NodeJS module](http://nodejs.org/api/child_process.html#child_process_class_childprocess).

----

A common [convention](http://docs.nodejitsu.com/articles/errors/what-are-the-error-conventions) used in NodeJS is the way `callback` functions are defined.  Usually, they look like this:
```javascript
function callback(error, data) {...}
```
```coffeescript
callback = (error, data) -> ...
```
If an error is encountered in an I/O function, instead of throwing an error for you, it calls the `callback` with an error object as the first argument.  There are two main reasons this is done:
 
 1. You don't have to riddle your code with `try` and `catch` blocks.
 2. You have more flexibility in handling the error how you want.
  <br /><br />

Your function should follow this convention when calling `callback`.  So if you encounter an error, instead of throwing it, call `callback` with the `error` object as the first argument.  If you do *not* encounter an error, call `callback` with the first argument as `null`, and the second argument as the returned string from the command.

----

###Code Examples
```javascript
//Where 'err' is the error Child Process sends:

execute('echo hi', cb)
  // calls cb(null, 'hi') if no error
  // calls cb(err) if there is an error

execute('expr 1 + 2', cb)
  // calls cb(null, '3') if no error
  // calls cb(err) if there is an error
```

```coffeescript
#Where 'err' is the error Child Process sends:

execute('echo hi', cb)
  #calls cb(null, 'hi') if no error
  #calls cb(err) if there is an error

execute('expr 1 + 2', cb)
  #calls cb(null, '3') if no error
  #calls cb(err) if there is an error    
```
---

###Tips

Test cases *will* make check to ensure you are passing an error object back, so make sure you are passing the error instead of `throw`ing it.  Also, make sure when you do pass an error, you halt code execution in your function (1:1 ratio for `execute` and `callback` calls).

If you are confused about callbacks, here is a good article that explains them in more detail: [What are callbacks?](http://docs.nodejitsu.com/articles/getting-started/control-flow/what-are-callbacks).

Don't forget to look at the [Child Process Module documentation](http://nodejs.org/api/child_process.html#child_process_child_process_exec_command_options_callback).

Google is your friend, as is the [NodeJS Docs](http://nodejs.org/api/) :)
