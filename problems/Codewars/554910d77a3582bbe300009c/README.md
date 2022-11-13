[_metadata_:generated]: - "true"

# Who won the election?

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`554910d77a3582bbe300009c`](https://www.codewars.com/kata/554910d77a3582bbe300009c) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

In democracy we have a lot of elections. For example, we have to vote for a class representative in school, for a new parliament or a new government.

Usually, we vote for a candidate, i.e. a set of eligible candidates is given. This is done by casting a ballot into a ballot-box. After that, it must be counted how many ballots (= votes) a candidate got. 

A candidate will win this election if he has the <a href="https://en.wikipedia.org/wiki/Supermajority#Majority_of_the_entire_membership">absolute majority</a>.

<h2>Your Task</h2>
Return the name of the winner. If there is no winner, return <i>null</i> (in Java and JavaScript), <i>None</i> (in Python), <i>nil</i> (in Ruby), or <i> * </i>  in C.

<h2>Task Description</h2>
There are no given candidates. An elector can vote for anyone. Each ballot contains only one name and represents one vote for this name. A name is an arbitrary string, e.g. "A", "B", or "XJDHD".<br>
<br>
There are no spoiled ballots.<br>
<br>
The ballot-box is represented by an unsorted list of names. Each entry in the list corresponds to one vote for this name. You do not know the names in advance (because there are no candidates).<br>
<br>
A name wins the election if it gets more than n/2 votes (n = number of all votes, i.e. n is equal to the size of the given list). 

<h2>Examples</h2>

```java
//3 votes for "A", 2 votes for "B" -> "A" wins the election
BallotsCounter.getWinner(Arrays.asList("A", "A", "A", "B", "B")).equals("A") //true
//2 votes for "A", 2 votes for "B" -> No winner
BallotsCounter.getWinner(Arrays.asList("A", "A", "B", "B")) == null //true
//1 vote for each name -> No winner
BallotsCounter.getWinner(Arrays.asList("A", "B", "C", "D")) == null //true
//3 votes for "A", 2 votes for "B", 1 vote for "C"  
//-> No winner ("A" does not have more than n/2 = 3 votes)
BallotsCounter.getWinner(Arrays.asList("A", "A", "A", "B", "B", "C")) == null //true
```
```python
#3 votes for "A", 2 votes for "B" -> "A" wins the election
getWinner(["A", "A", "A", "B", "B"]) == "A" #true
#2 votes for "A", 2 votes for "B" -> No winner
getWinner(["A", "A", "B", "B"]) == None #true
#1 vote for each name -> No winner
getWinner(["A", "B", "C", "D"]) == None #true
#3 votes for "A", 2 votes for "B", 1 vote for "C"  
#-> No winner ("A" does not have more than n/2 = 3 votes)
getWinner(["A", "A", "A", "B", "B", "C"]) == None #true
```
```ruby
#3 votes for "A", 2 votes for "B" -> "A" wins the election
getWinner(["A", "A", "A", "B", "B"]) == "A" #true
#2 votes for "A", 2 votes for "B" -> No winner
getWinner(["A", "A", "B", "B"]) == nil #true
#1 vote for each name -> No winner
getWinner(["A", "B", "C", "D"]) == nil #true
#3 votes for "A", 2 votes for "B", 1 vote for "C"  
#-> No winner ("A" does not have more than n/2 = 3 votes)
getWinner(["A", "A", "A", "B", "B", "C"]) == nil #true
```
```javascript
//3 votes for "A", 2 votes for "B" -> "A" wins the election
getWinner(["A", "A", "A", "B", "B"]) === "A" //true
//2 votes for "A", 2 votes for "B" -> No winner
getWinner(["A", "A", "B", "B"]) === null //true
//1 vote for each name -> No winner
getWinner(["A", "B", "C", "D"]) === null //true
//3 votes for "A", 2 votes for "B", 1 vote for "C"  
//-> No winner ("A" does not have more than n/2 = 3 votes)
getWinner(["A", "A", "A", "B", "B", "C"]) === null //true
```

<h2>Note</h2>
Please keep in mind the list of votes can be large (n <= 1,200,000). The given list is immutable, i.e. you cannot modify the list (otherwise this could lead to vote rigging).

Good luck and have fun.
