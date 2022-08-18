[_metadata_:generated]: - "true"

# Sum The Tree

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5800580f8f7ddaea13000025`](https://www.codewars.com/kata/5800580f8f7ddaea13000025) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Given a node object representing a binary tree:

```javascript
Node:
  value: <int>,
  left: <Node> or null,
  right: <Node> or null
```
```c
Node:
  value: <int>,
  left: <Node> or null,
  right: <Node> or null
```
```cpp
struct node
{
  int value;
  node* left;
  node* right;
}
```
```csharp
public class Node
{  
    public int Value;  
    public Node Left;  
    public Node Right;
    
    public Node(int value, Node left = null, Node right = null)
    {
      Value = value;
      Left = left;
      Right = right;
    }
}  
```

write a function that returns the sum of all values, including the root. Absence of a node will be indicated with a `null` value.

Examples:
```
10
| \
1  2
=> 13

1
| \
0  0
    \
     2
=> 3
```
