[_metadata_:generated]: - "true"

# Smallest value of an array

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`544a54fd18b8e06d240005c0`](https://www.codewars.com/kata/544a54fd18b8e06d240005c0) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Write a function that can return the smallest value of an array or the index of that value. The function's 2nd parameter will tell whether it should return the value or the index.

Assume the first parameter will always be an array filled with at least 1 number and no duplicates. Assume the second parameter will be a string holding one of two values: 'value' and 'index'.

```javascript
min([1,2,3,4,5], 'value') // => 1
min([1,2,3,4,5], 'index') // => 0
```

```java
Arrays.findSmallest(new int[]{1,2,3,4,5}, 'value') // => 1
Arrays.findSmallest(new int[]{1,2,3,4,5}, 'index') // => 0
```

```C#
Kata.FindSmallest(new int[]{ 1, 2 , 3, 4, 5}, "value") // => 1
Kata.FindSmallest(new int[]{ 1, 2 , 3, 4, 5}, "index") // => 0
```
