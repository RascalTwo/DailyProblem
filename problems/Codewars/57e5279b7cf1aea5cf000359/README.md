[_metadata_:generated]: - "true"

# Fun with trees: max sum

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`57e5279b7cf1aea5cf000359`](https://www.codewars.com/kata/57e5279b7cf1aea5cf000359) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You are given a binary tree. Implement the method **maxSum** which returns the maximal sum of a route from root to leaf.
For example, given the following tree:
```
    17
   /  \
  3   -10
 /    /  \
2    16   1
         /
        13
```

The method should return 23, since [17,-10,16] is the route from root to leaf with the maximal sum.


The class TreeNode is available for you:

```java
class TreeNode {
    TreeNode left;
    TreeNode right;
    int value;
    ...
}
```
```csharp
class TreeNode
{
    public TreeNode left;
    public TreeNode right;
    public int value;
    ...
}
```
```cpp
class TreeNode
{
    public:
        TreeNode* left;
        TreeNode* right;
        int value;
    ...
};
```
```javascript
var TreeNode = function(value, left, right) {
  this.value = value;
  this.left = left;
  this.right = right;
};
```
```haskell
data TreeNode = Node TreeNode Int TreeNode | Leaf Int | None
```


This kata is part of [fun with trees](https://www.codewars.com/collections/fun-with-trees) series:

* [Fun with trees: max sum](https://www.codewars.com/kata/57e5279b7cf1aea5cf000359)
* [Fun with trees: array to tree](https://www.codewars.com/kata/57e5a6a67fbcc9ba900021cd)
* [Fun with trees: is perfect](https://www.codewars.com/kata/57dd79bff6df9b103b00010f)
