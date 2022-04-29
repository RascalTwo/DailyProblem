[_metadata_:generated]: - "true"

# Is every value in the array an array?

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`582c81d982a0a65424000201`](https://www.codewars.com/kata/582c81d982a0a65424000201) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Is every value in the array an array?

This should only test the second array dimension of the array. The values of the nested arrays don't have to be arrays. 

Examples:

```javascript
[[1],[2]] => true
['1','2'] => false
[{1:1},{2:2}] => false
```
```python
[[1],[2]] => true
['1','2'] => false
[{1:1},{2:2}] => false
```
```ruby
[[1],[2]] => true
['1','2'] => false
[{1:1},{2:2}] => false
```
```c
[[1],[2]] => true
['1','2'] => false
[{1:1},{2:2}] => false
```
```php
[[1], [2]] => true
["1", "2"] => false
[
  new class {
    public $one = 1;
  },
  new class {
    public $two = 2;
  }
] => false
```
