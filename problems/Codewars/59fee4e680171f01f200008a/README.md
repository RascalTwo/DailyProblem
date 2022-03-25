[_metadata_:generated]: - "true"

# Lua is easy: Lesson 1 - The basics

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`59fee4e680171f01f200008a`](https://www.codewars.com/kata/59fee4e680171f01f200008a) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924080/lua_neosme.svg" alt="Lua" title="Lua" width="50" />](solve.lua) |

<!-- INFO TABLE END -->

This Kata is part of `6` part series that will get you acquinted with Lua. At the end of lesson `6`, you should be able to attempt or translate any Kata to Lua. If you need to test your code before submitting, go to Lua's official demo [here](https://www.lua.org/cgi-bin/demo) and write tests in the editor and hit "RUN".

Lua is a dynamically-typed language, and it has eight basic types: `nil, Boolean, number, string, userdata, function, thread, and table`.

Variable declaration in Lua is straight forward. Consider the followng statements:
``` Lua
a = 10; b = 20 ; c = "I'm a string"; d = 'another string'; a = true; -- this is a comment

```

Math works the way you would expect it to, and we will cover this in [Lesson 3: Numbers](https://www.codewars.com/kata/59fefb39c374cbd056000052).
```Lua
+,/,*, ^(raise to power) , % (remainder),<, >, <=, >=, ==`, etc. 
```
Strings have many methods which we will cover in [Lesson 4: Strings](https://www.codewars.com/kata/59ff6308ba2a14f35800008f). For this Kata, we need to know that string concatenation is performed using two dots:
```Lua
print('Hello'..'World') --returns HelloWorld
print('Hello '..'World') -- returns "Hello World"
```

Consider the following function:
```Lua
function test (x)
  f = math.random(10) -- random number between 1 and 10, both inclusive  
  if f % 2 == 0 then return (f*x).." "..x.. " "..f
  else return "f is odd"
  end
end
--The result depends on the value of random number 'f'. It returns something like "32 8 4" if f is even else "f is odd".`  
--Notice the two 'end' keywords. One to close the if statement and the other to close the function.
```
The Kata for this first lesson is very basic, so please bear with it.  

You will write a simple function that takes `3` inputs `a, b, c` and returns `a` concatenated with `a * b` concatenated with `'Lua'` if `b >= c` otherwise `"Codewars"`. Seperate them with one space.

For example: 
```Lua
firstLua(1,2,3) --returns "1 2 Codewars"
firstLua(3,2,1) --returns "3 6 Lua"
```
In the next lesson, we will delve deeper into Numbers.

