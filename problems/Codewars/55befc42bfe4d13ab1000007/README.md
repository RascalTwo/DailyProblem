[_metadata_:generated]: - "true"

# Linked Lists - Get Nth Node

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`55befc42bfe4d13ab1000007`](https://www.codewars.com/kata/55befc42bfe4d13ab1000007) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Linked Lists - Get Nth

Implement a `GetNth()` function that takes a linked list and an integer index and returns the node stored at the `Nth` index position. `GetNth()` uses the C numbering convention that the first node is index 0, the second is index 1, ... and so on.

So for the list `42 -> 13 -> 666`, `GetNth(1)` should return `Node(13)`;

```javascript
getNth(1 -> 2 -> 3 -> null, 0).data === 1
getNth(1 -> 2 -> 3 -> null, 1).data === 2
```

```csharp
Node.GetNth(1 -> 2 -> 3 -> null, 0).Data == 1
Node.GetNth(1 -> 2 -> 3 -> null, 1).Data == 2
```

The index should be in the range `[0..length-1]`. If it is not, or if the list is empty, `GetNth()` should throw/raise an exception (`ArgumentException` in C#, `InvalidArgumentException` in PHP, `Exception` in Java).


**Related Kata in order of expected completion (increasing difficulty):**

* [Linked Lists - Push & BuildOneTwoThree](http://www.codewars.com/kata/linked-lists-push-and-buildonetwothree)
* [Linked Lists - Length & Count](http://www.codewars.com/kata/linked-lists-length-and-count)
* [Linked Lists - Get Nth Node](http://www.codewars.com/kata/linked-lists-get-nth-node)
* [Linked Lists - Insert Nth Node](http://www.codewars.com/kata/linked-lists-insert-nth-node)
* [Linked Lists - Sorted Insert](http://www.codewars.com/kata/linked-lists-sorted-insert) 
* [Linked Lists - Insert Sort](http://www.codewars.com/kata/linked-lists-insert-sort)
* [Linked Lists - Append](http://www.codewars.com/kata/linked-lists-append)
* [Linked Lists - Remove Duplicates](http://www.codewars.com/kata/linked-lists-remove-duplicates)
* [Linked Lists - Move Node](http://www.codewars.com/kata/linked-lists-move-node)
* [Linked Lists - Move Node In-place](http://www.codewars.com/kata/linked-lists-move-node-in-place)
* [Linked Lists - Alternating Split](http://www.codewars.com/kata/linked-lists-alternating-split)
* [Linked Lists - Front Back Split](http://www.codewars.com/kata/linked-lists-front-back-split)
* [Linked Lists - Shuffle Merge](http://www.codewars.com/kata/linked-lists-shuffle-merge)
* [Linked Lists - Sorted Merge](http://www.codewars.com/kata/linked-lists-sorted-merge)
* [Linked Lists - Merge Sort](http://www.codewars.com/kata/linked-lists-merge-sort)
* [Linked Lists - Sorted Intersect](http://www.codewars.com/kata/linked-lists-sorted-intersect)
* [Linked Lists - Iterative Reverse](http://www.codewars.com/kata/linked-lists-iterative-reverse)
* [Linked Lists - Recursive Reverse](http://www.codewars.com/kata/linked-lists-recursive-reverse)

Inspired by Stanford Professor Nick Parlante's excellent [Linked List teachings.](http://cslibrary.stanford.edu/103/LinkedListBasics.pdf)

http://cslibrary.stanford.edu/103/LinkedListBasics.pdf

http://cslibrary.stanford.edu/105/LinkedListProblems.pdf
