[_metadata_:generated]: - "true"

# Javascript filter - 2

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5262fa26875ed24a3e000029`](https://www.codewars.com/kata/5262fa26875ed24a3e000029) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

A friend of yours is developing an application for a hotel. You should write a function that returns all names of the people on a given floor. Every floor has 6 rooms, and all rooms are numbered in a consecutive way.

The function has the following signature:

```
function roomMates( rooms, floor ){}
```

The argument *rooms* holds all clients in an array, where the index (starts at 0) corresponds to the room-number and holds the name of the client.

A room is empty if the name at the corresponding array index is the empty string.

*floor* is an integer and denotes the floor whose names need to be returned. Floors are numbered starting at 1.

Your task is to return the names of all occupants on a given floor.

### Example

```
rooms = [ "Jill", "Jackson", "Jan", "Eve", "", "John", "Jimmy", "Tom", "", "Duke" ]
```

<table style="width:100%">
  <tr>
    <th>Floor</th>
    <th>Index/Room No.<th>
    <th>Name</th>
  </tr>
  <tr>
    <td>1</td>
    <td>0</td>
    <td>Jill</td>
  </tr>
  <tr>
    <td>1</td>
    <td>1</td>
    <td>Jackson</td>
  </tr>
  <tr>
    <td>1</td>
    <td>2</td>
    <td>Jan</td>
  </tr>
  <tr>
    <td>1</td>
    <td>3</td>
    <td>Eve</td>
  </tr>
  <tr>
    <td>1</td>
    <td>4</td>
    <td>(empty)</td>
  </tr>
  <tr>
    <td>1</td>
    <td>5</td>
    <td>John</td>
  </tr>
    <tr>
    <td>2</td>
    <td>6</td>
    <td>Jimmy</td>
  </tr>
    <tr>
    <td>2</td>
    <td>7</td>
    <td>Tom</td>
  </tr>
    <tr>
    <td>2</td>
    <td>8</td>
    <td>(empty)</td>
  </tr>
  <tr>
    <td>2</td>
    <td>9</td>
    <td>Duke</td>
  </tr>
</table>

`function roomMates( rooms, 1 )` should return `["Jill", "Jackson", "Jan", "Eve", "John"]`, and
`function roomMates( rooms, 2 )` should return `["Jimmy", "Tom", "Duke"]`.

<hr>

Hint: the filter-method of Javascript is handy here, which returns each element of the array for which the filter-method returns true. The second argument gives the index you're looking at:

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter
