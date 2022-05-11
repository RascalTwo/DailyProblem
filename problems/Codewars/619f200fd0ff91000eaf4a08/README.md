[_metadata_:generated]: - "true"

# Odd or Even? Determine that!

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`619f200fd0ff91000eaf4a08`](https://www.codewars.com/kata/619f200fd0ff91000eaf4a08) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

### Task

Given a number `N`, determine if the sum of `N` ***consecutive numbers*** is odd or even.

- If the sum is definitely an odd number, return `Odd`.  
- If the sum is definitely an even number, return `Even`.  
- If the sum can be either odd or even ( depending on which first number you choose ), return `Either`.  

### Examples

- `Odd_or_Even(1)` should return `Either`, because the sum can be odd or even.  
- `Odd_or_Even(6)` should return `Odd`, because `6` consecutive numbers contain `3` odd and `3` even numbers, so their sum is always odd.  
- `Odd_or_Even(8)` should return `Even`, because `8` consecutive numbers contain `4` odd and `4` even numbers, so their sum is always even.  

~~~if:cpp
### Note
```cpp
enum { Even, Odd, Either };
```
is `Preloaded`.
~~~

~~~if:c
### Note
```c
enum { EVEN, ODD, EITHER };
```
is `Preloaded`.
~~~

~~~if:nasm
### Note
```nasm
%define EVEN    0
%define ODD     1
%define EITHER  2
```
is `Preloaded`.
~~~

~~~if:javascript
### Note
```javascript
const ODD = "Odd";
const EVEN = "Even";
const EITHER = "Either";
```
is `Preloaded`.
~~~

~~~if:haskell
### Note
```haskell
data Parity = EITHER | EVEN | ODD
```
is `Preloaded`.
~~~
