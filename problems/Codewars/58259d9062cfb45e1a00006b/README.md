[_metadata_:generated]: - "true"

# Fun with lists: map

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`58259d9062cfb45e1a00006b`](https://www.codewars.com/kata/58259d9062cfb45e1a00006b) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Implement the method **map**, which accepts a linked list (head) and a mapping function, and returns a new linked list (head) where every element is the result of applying the given mapping method to each element of the original list.

For example:
Given the list: `1 -> 2 -> 3`, and the mapping function `x => x * 2`, **map** should return `2 -> 4 -> 6`

The linked list is defined as follows:

```javascript
function Node(data, next = null) {
  this.data = data;
  this.next = next;
}
```
```java
class Node<T> {
  public T data;
  public Node<T> next;
  
  Node(T data, Node next) {
    this.data = data;
    this.next = next;
  }
  
  Node(T data) {
    this(data, null);
  }
}
```
```php
class Node {
  public $data, $next;
  public function __construct($data, $next = NULL) {
    $this->data = $data;
    $this->next = $next;
  }
}
```
```csharp
class Node<T> 
{
    public T data;
    public Node<T> next;
    
    public Node<T>(T data){
        this.data = data;
    }
    
    public Node<T>(T data, Node<T> next){
        this.data = data;
        this.next = next;
    }
}
```
```c
struct Node {
  struct Node *next;
  int data;
};
```

Note: the list may be null and can hold any type of value.

Good luck!


This kata is part of [fun with lists](https://www.codewars.com/collections/fun-with-lists) series:

* [Fun with lists: length](https://www.codewars.com/kata/581e476d5f59408553000a4b)
* [Fun with lists: indexOf](https://www.codewars.com/kata/581c6b075cfa83852700021f)
* [Fun with lists: lastIndexOf](https://www.codewars.com/kata/581c867a33b9fe732e000076)
* [Fun with lists: countIf](https://www.codewars.com/kata/5819081d056d4bdd410004f8)
* [Fun with lists: anyMatch + allMatch](https://www.codewars.com/kata/581e50555f59405743001813)
* [Fun with lists: filter](https://www.codewars.com/kata/582041237df353e01d000084)
* [Fun with lists: map](https://www.codewars.com/kata/58259d9062cfb45e1a00006b)
* [Fun with lists: reduce](https://www.codewars.com/kata/58319f37aeb69a89a00000c7)
