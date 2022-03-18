[_metadata_:generated]: - "true"

# String repeat

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`57a0e5c372292dd76d000d7e`](https://www.codewars.com/kata/57a0e5c372292dd76d000d7e) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

~~~if-not:racket,bf
Write a function called `repeatStr` which repeats the given string `string` exactly `n` times.
~~~
~~~if:racket
Write a function called `repeat-string` which repeats the given string `str` exactly `count` times.
~~~
~~~if:bf
Write a program which accepts a single byte `n` and then a sequence of bytes `string` and outputs the `string` exactly `n` times.

The first input byte will be `n`. Following bytes will be characters of `string`. The end of the input `string` will be indicated with a null byte `\0`.
~~~

```c
repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
```
```cpp
repeat_str(6, "I") // "IIIIII"
repeat_str(5, "Hello") // "HelloHelloHelloHelloHello"
```
```dart
repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
```

```reason
repeatStr(6, "I") /* "IIIIII" */
repeatStr(5, "Hello") //*"HelloHelloHelloHelloHello" */
```
```factor
6 "I" repeat-str ! "IIIIII"
5 "Hello" repeat-str ! "HelloHelloHelloHelloHello"
```

```lua
repeatStr(6, "I") -- "IIIIII"
repeatStr(5, "Hello") -- "HelloHelloHelloHelloHello"
```

```elixir
repeat_str(6, "I") # "IIIIII"
repeat_str(5, "Hello") # "HelloHelloHelloHelloHello"
```

```scala
StringRepeat.repeatStr(6, "I") # "IIIIII"
StringRepeat.repeatStr(5, "Hello") # "HelloHelloHelloHelloHello"
```

```nim
repeatStr(6, "I") # "IIIIII"
repeatStr(5, "Hello") # "HelloHelloHelloHelloHello"
```

```julia
repeatstr(6, "I") # "IIIIII"
repeatstr(5, "Hello") # "HelloHelloHelloHelloHello"
```

```kotlin
repeatstr(6, "I") // "IIIIII"
repeatstr(5, "Hello") // "HelloHelloHelloHelloHello"
```

```dart
repeatString(6, "I") // "IIIIII"
repeatString(5, "Hello") // "HelloHelloHelloHelloHello"
```
```racket
(repeat-string 6 "I") ; "IIIIII"
(repeat-string 5 "Hello") ; "HelloHelloHelloHelloHello"
```
```perl
Kata::repeat_str(6, "I") # "IIIIII"
Kata::repeat_str(5, "Hello") # "HelloHelloHelloHelloHello"
```
```bf
"\6I" -> "IIIIII"
"\5Hello" -> "HelloHelloHelloHelloHello"
```
```cobol
      RepeatString(6, "I")
      * ->   "IIIIII"
      RepeatString(5, "Hello")
      * ->  "HelloHelloHelloHelloHello"
```
