[_metadata_:generated]: - "true"

# What comes after? 

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`590f5b4a7bbb3e246000007d`](https://www.codewars.com/kata/590f5b4a7bbb3e246000007d) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You will be given two inputs: a string of words and a letter. For each string, return the alphabetic character after every instance of letter(case insensitive). 

If there is a number, punctuation or underscore following the letter, it should not be returned. 

```
If letter = 'r':
comes_after("are you really learning Ruby?") # => "eenu"
comes_after("Katy Perry is on the radio!")   # => "rya"
comes_after("Pirates say arrrrrrrrr.")       # => "arrrrrrrr"
comes_after("r8 your friend")                # => "i"
```

Return an empty string if there are no instances of `letter` in the given string.

Adapted from: [Ruby Kickstart](https://github.com/JoshCheek/ruby-kickstart/blob/master/session1/challenge/7_string.rb)
