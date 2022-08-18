[_metadata_:generated]: - "true"

# We Have Liftoff

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`53d6387b83db278202000802`](https://www.codewars.com/kata/53d6387b83db278202000802) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You have an array of numbers 1 through n (where 1 <= n <= 10). The array needs to be formatted correctly for the person reading the countdown of a spaceship launch.

Unfortunately, the person reading the countdown only knows how to read strings.  After the array is sorted correctly make sure it's in a format he can understand.

Between each number should be a space and after the final number (n) should be the word 'liftoff!'

Example:
```ruby
# Given
instructions = [8,1,10,2,7,9,6,3,4,5]
# Should return
"10 9 8 7 6 5 4 3 2 1 liftoff!"
```
```javascript
// Given
instructions = [8,1,10,2,7,9,6,3,4,5]
// Should return
"10 9 8 7 6 5 4 3 2 1 liftoff!"
// Given
instructions = [1,2,4,3,5]
// Should return
"5 4 3 2 1 liftoff!"
```
```csharp
Kata.Liftoff(new List<int> {2, 8, 10, 9, 1, 3, 4, 7, 6, 5}) => "10 9 8 7 6 5 4 3 2 1 liftoff!"
```
