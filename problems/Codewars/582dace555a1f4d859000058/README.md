[_metadata_:generated]: - "true"

# Coding Meetup #12 - Higher-Order Functions Series - Find GitHub admins

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`582dace555a1f4d859000058`](https://www.codewars.com/kata/582dace555a1f4d859000058) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You will be given an array of objects representing data about developers who have signed up to attend the next coding meetup that you are organising.

Given the following input array:

```javascript
var list1 = [
  { firstName: 'Harry', lastName: 'K.', country: 'Brazil', continent: 'Americas', age: 22, language: 'JavaScript', githubAdmin: 'yes' },
  { firstName: 'Kseniya', lastName: 'T.', country: 'Belarus', continent: 'Europe', age: 49, language: 'Ruby', githubAdmin: 'no' },
  { firstName: 'Jing', lastName: 'X.', country: 'China', continent: 'Asia', age: 34, language: 'JavaScript', githubAdmin: 'yes' },
  { firstName: 'Piotr', lastName: 'B.', country: 'Poland', continent: 'Europe', age: 128, language: 'JavaScript', githubAdmin: 'no' }
];
```

```python
list1 = [
  { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes' },
  { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 49, 'language': 'Ruby', 'githubAdmin': 'no' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes' },
  { 'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128, 'language': 'JavaScript', 'githubAdmin': 'no' }
  ]
```
```cobol
       01  list1.
          03  ListLength      pic 9(2) value 4.
          03  dev1.
              05 FirstName    pic a(9)  value 'Harry'.
              05 LastName     pic x(2)  value 'K.'.
              05 Country      pic a(24) value 'Brazil'.
              05 Continent    pic a(8)  value 'Americas'.
              05 Age          pic 9(3)  value 22.
              05 Language     pic a(10) value 'JavaScript'.
              05 GithubAdmin  pic a(3)  value 'yes'.
          03  dev2.
              05 FirstName    pic a(9)  value 'Kseniya'.
              05 LastName     pic x(2)  value 'T.'.
              05 Country      pic a(24) value 'Belarus'.
              05 Continent    pic a(8)  value 'Europe'.
              05 Age          pic 9(3)  value 49.
              05 Language     pic a(10) value 'Ruby'.
              05 GithubAdmin  pic a(3)  value 'no'.
          03  dev3.
              05 FirstName    pic a(9)  value 'Jing'.
              05 LastName     pic x(2)  value 'X.'.
              05 Country      pic a(24) value 'China'.
              05 Continent    pic a(8)  value 'Asia'.
              05 Age          pic 9(3)  value 34.
              05 Language     pic a(10) value 'JavaScript'.
              05 GithubAdmin  pic a(3)  value 'yes'.
          03  dev4.
              05 FirstName    pic a(9)  value 'Piotr'.
              05 LastName     pic x(2)  value 'B.'.
              05 Country      pic a(24) value 'Poland'.
              05 Continent    pic a(8)  value 'Europe'.
              05 Age          pic 9(3)  value 128.
              05 Language     pic a(10) value 'JavaScript'.
              05 GithubAdmin  pic a(3)  value 'no'.

```

write a function that when executed as `findAdmin(list1, 'JavaScript')` returns only the JavaScript developers who are GitHub admins:

```javascript
[
  { firstName: 'Harry', lastName: 'K.', country: 'Brazil', continent: 'Americas', age: 22, language: 'JavaScript', githubAdmin: 'yes' },
  { firstName: 'Jing', lastName: 'X.', country: 'China', continent: 'Asia', age: 34, language: 'JavaScript', githubAdmin: 'yes' }
]
```

```python
[
  { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes' }
]
```

```cobol
      01  result.
          03  ResLength       pic 9(2) value 2.
          03  .
              05 FirstName    pic a(9)  value 'Harry'.
              05 LastName     pic x(2)  value 'K.'.
              05 Country      pic a(24) value 'Brazil'.
              05 Continent    pic a(8)  value 'Americas'.
              05 Age          pic 9(3)  value 22.
              05 Language     pic a(10) value 'JavaScript'.
              05 GithubAdmin  pic a(4)  value 'yes'.
          03  .
              05 FirstName    pic a(9)  value 'Jing'.
              05 LastName     pic x(2)  value 'X.'.
              05 Country      pic a(24) value 'China'.
              05 Continent    pic a(8)  value 'Asia'.
              05 Age          pic 9(3)  value 34.
              05 Language     pic a(10) value 'JavaScript'.
              05 GithubAdmin  pic a(4)  value 'yes'.
```


Notes:

 - The original order should be preserved.
 - If there are no GitHub admin developers in a given language then return an empty array `[]`.
 - The input array will always be valid and formatted as in the example above.
 - The strings representing whether someone is a GitHub admin will always be formatted as `'yes'` and `'no'` (all lower-case).
 - The strings representing a given language will always be formatted in the same way (e.g. `'JavaScript'` will always be formatted with upper-case 'J' and 'S'.
<br>
<br>
<br>
<br>
<br>

This kata is part of the **Coding Meetup** series which includes a number of short and easy to follow katas which have been designed to allow mastering the use of higher-order functions. In JavaScript this includes methods like: `forEach, filter, map, reduce, some, every, find, findIndex`. Other approaches to solving the katas are of course possible.

Here is the full list of the katas in the **Coding Meetup** series:

<a href="http://www.codewars.com/kata/coding-meetup-number-1-higher-order-functions-series-count-the-number-of-javascript-developers-coming-from-europe">Coding Meetup #1 - Higher-Order Functions Series - Count the number of JavaScript developers coming from Europe</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-2-higher-order-functions-series-greet-developers">Coding Meetup #2 - Higher-Order Functions Series - Greet developers</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-3-higher-order-functions-series-is-ruby-coming">Coding Meetup #3 - Higher-Order Functions Series - Is Ruby coming?</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-4-higher-order-functions-series-find-the-first-python-developer">Coding Meetup #4 - Higher-Order Functions Series - Find the first Python developer</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-5-higher-order-functions-series-prepare-the-count-of-languages">Coding Meetup #5 - Higher-Order Functions Series - Prepare the count of languages</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-6-higher-order-functions-series-can-they-code-in-the-same-language">Coding Meetup #6 - Higher-Order Functions Series - Can they code in the same language?</a>

<a href="http://www.codewars.com/kata/coding-meetup-number-7-higher-order-functions-series-find-the-most-senior-developer">Coding Meetup #7 - Higher-Order Functions Series - Find the most senior developer</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-8-higher-order-functions-series-will-all-continents-be-represented">Coding Meetup #8 - Higher-Order Functions Series - Will all continents be represented?</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-9-higher-order-functions-series-is-the-meetup-age-diverse">Coding Meetup #9 - Higher-Order Functions Series - Is the meetup age-diverse?</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-10-higher-order-functions-series-create-usernames">Coding Meetup #10 - Higher-Order Functions Series - Create usernames</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-11-higher-order-functions-series-find-the-average-age">Coding Meetup #11 - Higher-Order Functions Series - Find the average age</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-12-higher-order-functions-series-find-github-admins">Coding Meetup #12 - Higher-Order Functions Series - Find GitHub admins</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-13-higher-order-functions-series-is-the-meetup-language-diverse">Coding Meetup #13 - Higher-Order Functions Series - Is the meetup language-diverse?</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-14-higher-order-functions-series-order-the-food">Coding Meetup #14 - Higher-Order Functions Series - Order the food</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-15-higher-order-functions-series-find-the-odd-names">Coding Meetup #15 - Higher-Order Functions Series - Find the odd names</a>

<a href="https://www.codewars.com/kata/coding-meetup-number-16-higher-order-functions-series-ask-for-missing-details">Coding Meetup #16 - Higher-Order Functions Series - Ask for missing details</a>
