[_metadata_:generated]: - "true"

# Convert a linked list to a string

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`582c297e56373f0426000098`](https://www.codewars.com/kata/582c297e56373f0426000098) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Convert a linked list to a string

## Related Kata

Although this Kata is not part of an official Series, you may also want to try out [Parse a linked list from a string](https://www.codewars.com/kata/582c5382f000e535100001a7) if you enjoyed this Kata.

## Preloaded

Preloaded for you is a class, struct or derived data type `Node` ( depending on the language ) used to construct linked lists in this Kata:

<!-- unlisted languages use the top block -- please keep c up top -->

```c
typedef struct node {
  int data;
  struct node *next;
} Node;
```
```cobol
      * Defined in the linkage section
       01  node.
           05 val     pic 9(4).
           05 nxt     usage pointer.
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
```javascript
class Node {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }
}
```
```csharp
public class Node {
  public int Data { get; private set; }
  public Node Next { get; private set; }

  public Node(int data, Node next = null) {
    Data = data;
    Next = next;
  }
}
```
```python
class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
```
```java
class Node {
	private int data;
	private Node next;
	
	public Node(int data, Node next) {
		this.data = data;
		this.next = next;
	}
	
	public Node(int data) {
		this.data = data;
		this.next = null;
	}

	public int getData() {
		return data;
	}

	public Node getNext() {
		return next;
	}
}
```
```ruby
class Node
  attr_reader :data, :next_node
  
  def initialize(data, next_node=nil)
    @data = data
    @next_node = next_node
  end
end
```
```cpp
class Node
{
  public:
    int data;
    Node* next;
  
  Node(int data, Node* next = nullptr)
  {
    this->data = data;
    this->next = next;
  }
};
```
```haskell
-- use regular lists, which are already singly-linked
data [a] = [] | a : [a]
```
```objc
typedef struct node {
  int data;
  struct node *next;
} Node;
```
```fortran
type Node
  integer :: data
  type(Node), pointer :: next
end type Node
```
```factor
SYMBOL: +nil+
TUPLE: node data next ;
C: <node> node
```

~~~if:objc
*NOTE: In Objective-C, the* `Node` *struct is placed on top of your main solution because there is a "double-import" bug in the Preloaded section at the time of writing (which cannot be fixed on my end).  Attempts to modify it (e.g. to cheat the tests in some way) will likely result in a test crash so it is not recommended for you to modify that section ;)*
~~~

~~~if:c
*NOTE: In C, the* `Node` *struct is placed on top of your main solution (and the [Sample] Test Cases) because the compiler complains about not recognizing the* `Node` *datatype even after adding it to the Preloaded section.  Attempts to modify it (e.g. to cheat the tests in some way) will likely result in a test crash so it is not recommended for you to modify that section ;)*
~~~

~~~if:nasm
When attempting this Kata in NASM, note that the code example shown directly above may not be relevant; please refer to the Sample Tests (written in C) for the exact definition of the `Node` structure.
~~~

## Prerequisites

This Kata assumes that you are already familiar with the idea of a linked list.  If you do not know what that is, you may want to read [this article on Wikipedia](https://en.wikipedia.org/wiki/Linked_list).  Specifically, the linked lists this Kata is referring to are **singly linked lists**, where the value of a specific node is stored in its `data` / `$data` / `Data` property, the reference to the next node is stored in its `next` / `$next` / `Next` / `next_node` property and the terminator for a list is `null` / `NULL` / `None` / `nil` / `nullptr` / `null()`.

## Task

~~~if:nasm
*If you are attempting this Kata in NASM, the code examples shown below may not be relevant at all - please refer to the Sample Tests (written in C) for the exact requirements.*
~~~

Create a function `stringify` which accepts an argument `list` / `$list` and returns a string representation of the list.  The string representation of the list starts with the value of the current `Node`, specified by its `data` / `$data` / `Data` property, followed by a whitespace character, an arrow and another whitespace character (`" -> "`), followed by the rest of the list.  The end of the string representation of a list must always end with `null` / `NULL` / `None` / `nil` / `nullptr` / `null()` ( all caps or all lowercase depending on the language you are undertaking this Kata in ).  For example, given the following list:

<!-- unlisted languages use the top block -- please keep c up top -->

```c
&((Node){
  .data = 1,
  .next = &((Node){
    .data = 2,
    .next = &((Node){
      .data = 3,
      .next = NULL
    })
  })
})
```
```php
new Node(1, new Node(2, new Node(3)))
```
```javascript
new Node(1, new Node(2, new Node(3)))
```
```csharp
new Node(1, new Node(2, new Node(3)))
```
```python
Node(1, Node(2, Node(3)))
```
```java
new Node(1, new Node(2, new Node(3)))
```
```ruby
Node.new(1, Node.new(2, Node.new(3)))
```
```cpp
new Node(1, new Node(2, new Node(3)))
```
```haskell
[1,2,3]
```
```objc
&((Node){
  .data = 1,
  .next = &((Node){
    .data = 2,
    .next = &((Node){
      .data = 3,
      .next = NULL
    })
  })
})
```
```fortran
type(Node), pointer :: oneTwoThree
! Where:
! oneTwoThree%data == 1
! oneTwoThree%next%data == 2
! oneTwoThree%next%next%data == 3
! oneTwoThree%next%next%next => null()
```
```factor
1 2 3 +nil+ <node> <node> <node>
```
```cobol
       01 node1.
         05 val pic 9(4) value 1.
         05 nxt usage pointer.
       01 node2.
         05 val pic 9(4) value 2.
         05 nxt usage pointer.
       01 node3.
         05 val pic 9(4) value 3.
         05 nxt usage pointer value null.
       ...
       set nxt of node1 to address of node2
       set nxt of node2 to address of node3
```

... its string representation would be:

<!-- unlisted languages use the top block -- please keep javascript up top -->

```javascript
"1 -> 2 -> 3 -> null"
```
```php
"1 -> 2 -> 3 -> NULL"
```
```c
"1 -> 2 -> 3 -> NULL"
```
```python
"1 -> 2 -> 3 -> None"
```
```ruby
"1 -> 2 -> 3 -> nil"
```
```cpp
"1 -> 2 -> 3 -> nullptr"
```
```objc
@"1 -> 2 -> 3 -> NULL"
```
```fortran
"1 -> 2 -> 3 -> null()"
```
```factor
"1 -> 2 -> 3 -> +nil+"
```
```cobol
       "1 -> 2 -> 3 -> NULL"
```

And given the following linked list:

<!-- unlisted languages use the top block -- please keep javascript up top -->

```javascript
new Node(0, new Node(1, new Node(4, new Node(9, new Node(16)))))
```
```python
Node(0, Node(1, Node(4, Node(9, Node(16)))))
```
```ruby
Node.new(0, Node.new(1, Node.new(4, Node.new(9, Node.new(16)))))
```
```haskell
[ 0, 1, 4, 9, 16 ]
```
```objc
&((Node){
  .data = 0,
  .next = &((Node){
    .data = 1,
    .next = &((Node){
      .data = 4,
      .next = &((Node){
        .data = 9,
        .next = &((Node){
          .data = 16,
          .next = NULL
        })
      })
    })
  })
})
```
```c
&((Node){
  .data = 0,
  .next = &((Node){
    .data = 1,
    .next = &((Node){
      .data = 4,
      .next = &((Node){
        .data = 9,
        .next = &((Node){
          .data = 16,
          .next = NULL
        })
      })
    })
  })
})
```
```fortran
type(Node), pointer :: list
! Where:
! list%data == 0
! list%next%data == 1
! list%next%next%data == 4
! list%next%next%next%data == 9
! list%next%next%next%next%data == 16
! list%next%next%next%next%next => null()
```
```factor
0 1 4 9 16 +nil+ <node> <node> <node> <node> <node>
```
```cobol
       01 node1.
         05 val pic 9(4) value 0.
         05 nxt usage pointer.
       01 node2.
         05 val pic 9(4) value 1.
         05 nxt usage pointer.
       01 node3.
         05 val pic 9(4) value 4.
         05 nxt usage pointer.
       01 node4.
         05 val pic 9(4) value 9.
         05 nxt usage pointer.
       01 node5.
         05 val pic 9(4) value 16.
         05 nxt usage pointer value null.
       ...
       set nxt of node1 to address of node2
       set nxt of node2 to address of node3
       set nxt of node3 to address of node4
       set nxt of node4 to address of node5
```

... its string representation would be:

<!-- unlisted languages use the top block -- please keep javascript up top -->

```javascript
"0 -> 1 -> 4 -> 9 -> 16 -> null"
```
```php
"0 -> 1 -> 4 -> 9 -> 16 -> NULL"
```
```c
"0 -> 1 -> 4 -> 9 -> 16 -> NULL"
```
```python
"0 -> 1 -> 4 -> 9 -> 16 -> None"
```
```ruby
"0 -> 1 -> 4 -> 9 -> 16 -> nil"
```
```cpp
"0 -> 1 -> 4 -> 9 -> 16 -> nullptr"
```
```objc
@"0 -> 1 -> 4 -> 9 -> 16 -> NULL"
```
```fortran
"0 -> 1 -> 4 -> 9 -> 16 -> null()"
```
```factor
"0 -> 1 -> 4 -> 9 -> 16 -> +nil+"
```
```cobol
       "0 -> 1 -> 4 -> 9 -> 16 -> NULL"
```

Note that `null` / `NULL` / `None` / `nil` / `nullptr` / `null()` itself is also considered a valid linked list.  In that case, its string representation would simply be `"null"` / `"NULL"` / `"None"` / `"nil"` / `"nullptr"` / `@"NULL"` / `"null()"` ( again, depending on the language ).

For the simplicity of this Kata, you may assume that any `Node` in this Kata may only contain **non-negative integer** values.  For example, you will not encounter a `Node` whose `data` / `$data` / `Data` property is `"Hello World"`.

Enjoy, and don't forget to check out my other Kata Series :D

~~~if:fortran
_NOTE: In Fortran, your returned string is_ **not** _permitted to contain any leading and/or trailing whitespace._
~~~
