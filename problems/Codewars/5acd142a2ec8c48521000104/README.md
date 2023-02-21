[_metadata_:generated]: - "true"

# One line task: Square Every Digit

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5acd142a2ec8c48521000104`](https://www.codewars.com/kata/5acd142a2ec8c48521000104) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Inspired by <a href="https://www.codewars.com/kata/square-every-digit/">Square Every Digit</a> (and by the inimitable myjinxin2015's many clever one-line kata), your goal here is precisely the same (to square every digit in the given number), in 36 or fewer characters (JavaScript), or 47 or fewer in Ruby 

(**Note: in Ruby, spaces do _not_ count towards your total-- within reason**. Spacing shouldn't be more than 30% of your total to avoid possible cheats). 

Your return value should be in integer format.

Your input will always be a valid, non-negative integer... no tricks!

**Bonus:** Can you get it down to 34 characters? (43 in Ruby!)

Note: Just as a head's up, numbers are > 2^31, so bitwise operators aren't viable. 

**Examples:**

```javascript
sd(0)=>    0
sd(64)=>   3616
sd(1111)=> 1111
sd(2222)=> 4444
sd(3333)=> 9999
sd(3212)=> 9414
sd(1234)=> 14916
sd(77455754)=> 4949162525492516
sd(99999999)=> 8181818181818181
```
```ruby
s(0)=>    0
s(64)=>   3616
s(1111)=> 1111
s(2222)=> 4444
s(3333)=> 9999
s(3212)=> 9414
s(1234)=> 14916
s(77455754)=> 4949162525492516
s(99999999)=> 8181818181818181
```

P.S., if you can get the sample tests to pass while under the character limit, the full tests should pass without a hitch!

Have fun, and please upvote if you enjoyed it :)

Found this one too easy?  <a href="https://www.codewars.com/kata/5a905291fd57772be0000039">This one's a bit more difficult!</a>
<br>
Too hard? <a href="https://www.codewars.com/kata/one-line-task-square-a-number-without-star-plus-or-math-dot-pow">This one's a bit easier</a> :)
