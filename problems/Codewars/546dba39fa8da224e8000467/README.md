[_metadata_:generated]: - "true"

# Run-length encoding

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`546dba39fa8da224e8000467`](https://www.codewars.com/kata/546dba39fa8da224e8000467) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

> [Run-length encoding](https://en.wikipedia.org/w/index.php?title=Run-length_encoding) (RLE) is a very simple form of data compression in which runs of data (that is, sequences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the original run. <cite>Wikipedia</cite>

## Task

Your task is to write such a run-length encoding. For a given string, return a list (or array) of pairs (or arrays) 
[
 (i<sub>1</sub>, s<sub>1</sub>),
 (i<sub>2</sub>, s<sub>2</sub>),
 …,
 (i<sub>n</sub>, s<sub>n</sub>)
], such that one can reconstruct the original string by replicating the character s<sub>x</sub> i<sub>x</sub> times and concatening all those strings. Your run-length encoding should be minimal, ie. for all i the values s<sub>i</sub> and s<sub>i+1</sub> should differ.

## Examples

As the article states, RLE is a _very_ simple form of data compression. It's only suitable for runs of data, as one can see in the following example:

```haskell
runLengthEncoding "hello world!" 
        `shouldBe` [(1,'h'), (1,'e'), (2,'l'), (1,'o'), (1,' '), (1,'w'),(1,'o'), (1,'r'), (1,'l'), (1,'d'), (1,'!')]
```
```coffeescript
runLengthEncoding "hello world!"
 # =>      [[1,'h'], [1,'e'], [2,'l'], [1,'o'], [1,' '], [1,'w'], [1,'o'], [1,'r'], [1,'l'], [1,'d'], [1,'!']]
```
```javascript
runLengthEncoding("hello world!")
 //=>      [[1,'h'], [1,'e'], [2,'l'], [1,'o'], [1,' '], [1,'w'], [1,'o'], [1,'r'], [1,'l'], [1,'d'], [1,'!']]
```
```python
run_length_encoding("hello world!")
 //=>      [[1,'h'], [1,'e'], [2,'l'], [1,'o'], [1,' '], [1,'w'], [1,'o'], [1,'r'], [1,'l'], [1,'d'], [1,'!']]
```
```ruby
rle("hello world!")
 # => [[1,'h'], [1,'e'], [2,'l'], [1,'o'], [1,' '], [1,'w'], [1,'o'], [1,'r'], [1,'l'], [1,'d'], [1,'!']]
```

It's very effective if the same data value occurs in many consecutive data elements:
```haskell
runLengthEncoding "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb" 
        `shouldBe` [(34,'a'), (3,'b')]
```
```coffeescript
runLengthEncoding "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb" 
 #  => [[34,'a'], [3,'b']]
```
```javascript
runLengthEncoding("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb")
 // => [[34,'a'], [3,'b']]
```
```python
run_length_encoding("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb")
# => [[34,'a'], [3,'b']]
```
```ruby
rle("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb")
# => [[34,'a'], [3,'b']]
```
