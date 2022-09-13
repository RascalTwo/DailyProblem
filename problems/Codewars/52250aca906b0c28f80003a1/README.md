[_metadata_:generated]: - "true"

# uniq -c (UNIX style)

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`52250aca906b0c28f80003a1`](https://www.codewars.com/kata/52250aca906b0c28f80003a1) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Implement a function which behaves like the 'uniq -c' command in UNIX. 

It takes as input a sequence and returns a sequence in which all duplicate elements following each other have been reduced to one instance together with the number of times a duplicate elements occurred in the original array.

## Example:

```javascript
['a','a','b','b','c','a','b','c'] --> [['a',2],['b',2],['c',1],['a',1],['b',1],['c',1]]
```

```python
['a','a','b','b','c','a','b','c'] --> [('a',2),('b',2),('c',1),('a',1),('b',1),('c',1)]
```
