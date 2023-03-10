[_metadata_:generated]: - "true"

# multiFilter

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`56a298b27e9e994977000023`](https://www.codewars.com/kata/56a298b27e9e994977000023) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Write a function called multiFilter which receives a variable number of filter functions. The function should return a function that receives one element (a compound filter function).


That is, if we have two functions:

```javascript
function isEven(el){
  return el % 2 === 0;
}
```
and

```javascript
function isGTten(el){
  return el > 10;
}
```

then

```javascript
[1,2,3,4,10,11,12,20,21,22].filter(multiFilter(isEven, isGTten));
```

should return `[12,20,22]`

## Additional Rules
`multiFilter` can't be implemented using loops like:

- `for`
- `while`
- `do while`

***WARNING***: Using ES6 features may break these rules because Babel can introduce some `for` loops when transpiling your code. Please, open an issue if it happens. 
