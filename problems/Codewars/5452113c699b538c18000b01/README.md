[_metadata_:generated]: - "true"

# Guess the number!

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5452113c699b538c18000b01`](https://www.codewars.com/kata/5452113c699b538c18000b01) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

The `Guesser` class is set up to generate a random number from 1-1000, and allows 10 guesses to get the number.

Your task is to write a method '`get_number`' (`Guesser.prototype.getNumber()` in javascript) inside the `Guesser` class (or its derived class in Java) to identify a random number from 1-1000.

You should use the method:
```ruby
guess number
```
```javascript
this.guess(number)
```
```java
guess(number)
```
Which will return either:
```
"Too high!" If the guess is too high.
"Too low!" If the guess is too low.
or "Correct!" If the guess is correct.
```

You can only call this method 10 times before an exception is raised.

