[_metadata_:generated]: - "true"

# Waiting room

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`542f0c36d002f8cd8a0005e5`](https://www.codewars.com/kata/542f0c36d002f8cd8a0005e5) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

There's a waiting room with N chairs set in single row. Chairs are consecutively numbered from 1 to N. First is closest to the entrance (which is exit as well).
 
For some reason people choose a chair in the following way

1. Find a place as far from other people as possible
2. Find a place as close to exit as possible

All chairs must be occupied before the first person will be served

So it looks like this for 10 chairs and 10 patients

<table>
<thead>
<tr>
  <th>Chairs</th>
  <th>1</th>
  <th>2</th>
  <th>3</th>
  <th>4</th>
  <th>5</th>
  <th>6</th>
  <th>7</th>
  <th>8</th>
  <th>9</th>
  <th>10</th>
<tr>
</thead>

<tbody>

<tr>
  <td>Patients</td>
  <td>1</td>
  <td>7</td>
  <td>5</td>
  <td>8</td>
  <td>3</td>
  <td>9</td>
  <td>4</td>
  <td>6</td>
  <td>10</td>
  <td>2</td>
</tr>

</tbody>

</table>

Your task is to find last patient's chair's number. 

```
Input: number of chairs N, an integer greater than 2.
Output: a positive integer, the last patient's chair number.
```

Have fun :)
