[_metadata_:generated]: - "true"

# The Supermarket Queue

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`57b06f90e298a7b53d000a86`](https://www.codewars.com/kata/57b06f90e298a7b53d000a86) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

### input
```if-not:c
* customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
* n: a positive integer, the number of checkout tills.
```
```if:c
* customers: a pointer to an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
* customers_length: the length of the array that `customers` points to.
* n: a positive integer, the number of checkout tills.
```

### output
The function should return an integer, the total time required.

-------------------------------------------

## Important
**Please look at the examples and clarifications below, to ensure you understand the task correctly :)**

-------

### Examples

```javascript
queueTime([5,3,4], 1)
// should return 12
// because when there is 1 till, the total time is just the sum of the times

queueTime([10,2,3,3], 2)
// should return 10
// because here n=2 and the 2nd, 3rd, and 4th people in the 
// queue finish before the 1st person has finished.

queueTime([2,3,10], 2)
// should return 12
```
```haskell
queueTime [5,3,4] 1
-- should return 12
-- because when there is 1 till, the total time is just the sum of the times

queueTime [10,2,3,3] 2
-- should return 10
-- because here n=2 and the 2nd, 3rd, and 4th people in the 
-- queue finish before the 1st person has finished.

queueTime [2,3,10] 2
-- should return 12
```
```python
queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the 
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12
```
```ruby
queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the 
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12
```
```cpp
queueTime(std::vector<int>{5,3,4}, 1)
// should return 12
// because when n=1, the total time is just the sum of the times

queueTime(std::vector<int>{10,2,3,3}, 2)
// should return 10
// because here n=2 and the 2nd, 3rd, and 4th people in the 
// queue finish before the 1st person has finished.

queueTime(std::vector<int>{2,3,10}, 2)
// should return 12
```
```fsharp
queueTime [5;3;4] 1
// should return 12
// because when there is 1 till, the total time is just the sum of the times

queueTime [10;2;3;3] 2
// should return 10
// because here n=2 and the 2nd, 3rd, and 4th people in the 
// queue finish before the 1st person has finished.

queueTime [2;3;10] 2
// should return 12
```
```c
int customers1[] = {5, 3, 4};
int customers1_length = 3;
int n1 = 1;
queueTime(customers1, customers1_length, n1)
// should return 12
// because when n=1, the total time is just the sum of the times

int customers2[] = {10, 2, 3, 3};
int customers2_length = 4;
int n2 = 2;
queueTime(customers2, customers2_length, n2)
// should return 10
// because here n=2 and the 2nd, 3rd, and 4th people in the 
// queue finish before the 1st person has finished.

int customers3[] = {2, 3, 10};
int customers3_length = 3;
int n3 = 2;
queueTime(customers3, customers3_length, n3)
// should return 12
```
```cobol
      QueueTime [5,3,4] 1 => 12
      * because when there is 1 till, the total time is just the sum of the times

      QueueTime [10,2,3,3] 2 => 10
      *  because here n=2 and the 2nd, 3rd, and 4th people in the 
      * queue finish before the 1st person has finished.

      QueueTime [2,3,10] 2 => 12
```

### Clarifications

 * There is only ONE queue serving many tills, and
 * The order of the queue NEVER changes, and
 * The front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.

N.B. You should assume that all the test input will be valid, as specified above.

P.S. The situation in this kata can be likened to the more-computer-science-related idea of a thread pool, with relation to running multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool

