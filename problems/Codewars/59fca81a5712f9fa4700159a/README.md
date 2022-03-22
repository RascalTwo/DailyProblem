[_metadata_:generated]: - "true"

# Convert to Binary

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`59fca81a5712f9fa4700159a`](https://www.codewars.com/kata/59fca81a5712f9fa4700159a) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Task Overview

Given a non-negative integer `n`, write a function `to_binary`/`ToBinary` which returns that number in a binary format.

<!-- C# documentation -->
```if:csharp
<h1>Documentation:</h1>
<h2>Kata.ToBinary Method (Int32)</h2>

Returns the binary representation of a non-negative integer as an integer.

<span style="font-size:20px">Syntax</span>
<div style="margin-top:-10px;padding:2px;background-color:Grey;position:relative;left:20px;width:600px;">
  <div style="background-color:White;color:Black;border:1px;display:block;padding:10px;padding-left:18px;font-family:Consolas,Courier,monospace;">
    <span style="color:Blue;">public</span>
    <span style="color:Blue;">static</span>
    <span style="color:Blue;">int</span> ToBinary(</br>
    <span style="position:relative;left:62px;">int n</span></br>
    )
  </div>
</div>
</br>
<div style="position:relative;left:20px;">
  <strong>Parameters</strong>
  </br>
  <i>n</i>
  </br>
  <span style="position:relative;left:50px;">Type: <a href="https://msdn.microsoft.com/en-us/library/system.int32(v=vs.110).aspx">System.Int32</a></span></br>
  <span style="position:relative;left:50px;">The integer to convert.</span>
  </br></br>
  <strong>Return Value</strong>
  </br>
  <span>Type: <a href="https://msdn.microsoft.com/en-us/library/system.int32(v=vs.110).aspx">System.Int32</a></span></br>
  The binary representation of the argument as an integer.
</div>
```
<!-- end C# documentation -->

<!-- C -->
```if:c
Example:
```
```c
to_binary(1)  /* should return 1 */
to_binary(5)  /* should return 101 */
to_binary(11) /* should return 1011 */
```
<!-- end of C -->

<!-- Javascript-->
```if:javascript
Example:
```
```javascript
toBinary(1)  /* should return 1 */
toBinary(5)  /* should return 101 */
toBinary(11) /* should return 1011 */
```
<!-- end of Javascript -->

<!-- NASM -->
```if:nasm
Example:
```
```nasm
mov di, 1
call to_binary    ; RAX <- 1

mov di, 5
call to_binary    ; RAX <- 101

mov di, 11
call to_binary    ; RAX <- 1011
```
<!-- end of NASM -->

<!-- Python -->
```if:Python
Example:
```
```python
to_binary(1)  # should return 1 
to_binary(5)  # should return 101
to_binary(11) # should return 1011
```
<!-- end of Python -->

<!-- Ruby-->
```if:ruby
Example:
```
```ruby
to_binary(1)  # should return 1
to_binary(5)  # should return 101
to_binary(11) # should return 1011
```
<!-- end of Ruby -->

<!-- Racket-->
```racket
(->binary 1)  ; 1
(->binary 5)  ; 101
(->binary 11) ; 1011
```
<!-- end of Racket -->


