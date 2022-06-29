[_metadata_:generated]: - "true"

# Custom each() Array method

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`513e7e1aee7d36073e00000d`](https://www.codewars.com/kata/513e7e1aee7d36073e00000d) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

JavaScript provides an Array.prototype.forEach method that allows you to iterate over array values. For this exercise  you will create your own array method called 'each'. It will be similar to the forEach method, except for one difference. If the callback function returns true then the loop will stop and no additional values will be iterated. 

The following shows a contrived example of how this new method would be used:
```javascript
var letters = ['a', 'b', 'c', 'd', 'e']
var allowedLetters = []
letters.each(function(letter, index){
  // break out of the loop if we reached a letter with the value 'd'
  if(letter == 'd') {
    return true;
  }
  allowedLetters.push(letter);   
})

// allowedLetters should equal ['a', 'b', 'c']
```
```ruby
letters = ['a', 'b', 'c', 'd', 'e']
allowedLetters = []

letters.each_until_true do |letter, index|
  # break out of the loop if we reached a letter with the value 'd'
  if letter == 'd'
    true
  else
    allowedLetters.push(letter);   
  end
end

# allowedLetters should equal ['a', 'b', 'c']
```
