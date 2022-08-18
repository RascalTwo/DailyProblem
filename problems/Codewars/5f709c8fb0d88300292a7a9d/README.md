[_metadata_:generated]: - "true"

# Who is the killer?

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5f709c8fb0d88300292a7a9d`](https://www.codewars.com/kata/5f709c8fb0d88300292a7a9d) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Who is the killer?
=
### Some people have been killed!
You have managed to narrow the suspects down to just a few. Luckily, you know every person who those suspects have seen on the day of the murders.

### Task.
Given a dictionary with all the names of the suspects and everyone that they have seen on that day which may look like this:
```python
{'James': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']}
```
```javascript
{'James': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']}
```
and also a list of the names of the dead people:
```python
['Lucas', 'Bill']
```
```javascript
['Lucas', 'Bill']
```
return the name of the one killer, in our case ```'James'``` because he is the only person that saw both ```'Lucas'``` and ```'Bill'```
