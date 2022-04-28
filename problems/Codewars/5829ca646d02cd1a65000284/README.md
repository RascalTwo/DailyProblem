[_metadata_:generated]: - "true"

# Coding Meetup #9 - Higher-Order Functions Series - Is the meetup age-diverse?

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5829ca646d02cd1a65000284`](https://www.codewars.com/kata/5829ca646d02cd1a65000284) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You will be given an array of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next coding meetup that you are organising.

Your task is to return:

- `true` if developers from all of the following age groups have signed up: teens, twenties, thirties, forties, fifties, sixties, seventies, eighties, nineties, centenarian (at least 100 years young). 
- `false` otherwise.

For example, given the following input array:

```javascript
var list1 = [
  { firstName: 'Harry', lastName: 'K.', country: 'Brazil', continent: 'Americas', age: 19, language: 'Python' },
  { firstName: 'Kseniya', lastName: 'T.', country: 'Belarus', continent: 'Europe', age: 29, language: 'JavaScript' },
  { firstName: 'Jing', lastName: 'X.', country: 'China', continent: 'Asia', age: 39, language: 'Ruby' },
  { firstName: 'Noa', lastName: 'A.', country: 'Israel', continent: 'Asia', age: 40, language: 'Ruby' },
  { firstName: 'Andrei', lastName: 'E.', country: 'Romania', continent: 'Europe', age: 59, language: 'C' },
  { firstName: 'Maria', lastName: 'S.', country: 'Peru', continent: 'Americas', age: 60, language: 'C' },
  { firstName: 'Lukas', lastName: 'X.', country: 'Croatia', continent: 'Europe', age: 75, language: 'Python' },
  { firstName: 'Chloe', lastName: 'K.', country: 'Guernsey', continent: 'Europe', age: 88, language: 'Ruby' },
  { firstName: 'Viktoria', lastName: 'W.', country: 'Bulgaria', continent: 'Europe', age: 98, language: 'PHP' },
  { firstName: 'Piotr', lastName: 'B.', country: 'Poland', continent: 'Europe', age: 128, language: 'JavaScript' }
];
```
```php
$list1 = [
  [
    "first_name" => "Harry",
    "last_name" => "K.",
    "country" => "Brazil",
    "continent" => "Americas",
    "age" => 19,
    "language" => "Python"
  ],
  [
    "first_name" => "Kseniya",
    "last_name" => "T.",
    "country" => "Belarus",
    "continent" => "Europe",
    "age" => 29,
    "language" => "JavaScript"
  ],
  [
    "first_name" => "Jing",
    "last_name" => "X.",
    "country" => "China",
    "continent" => "Asia",
    "age" => 39,
    "language" => "Ruby"
  ],
  [
    "first_name" => "Noa",
    "last_name" => "A.",
    "country" => "Israel",
    "continent" => "Asia",
    "age" => 40,
    "language" => "Ruby"
  ],
  [
    "first_name" => "Andrei",
    "last_name" => "E.",
    "country" => "Romania",
    "continent" => "Europe",
    "age" => 59,
    "language" => "C"
  ],
  [
    "first_name" => "Maria",
    "last_name" => "S.",
    "country" => "Peru",
    "continent" => "Americas",
    "age" => 60,
    "language" => "C"
  ],
  [
    "first_name" => "Lukas",
    "last_name" => "X.",
    "country" => "Croatia",
    "continent" => "Europe",
    "age" => 75,
    "language" => "Python"
  ],
  [
    "first_name" => "Chloe",
    "last_name" => "K.",
    "country" => "Guernsey",
    "continent" => "Europe",
    "age" => 88,
    "language" => "Ruby"
  ],
  [
    "first_name" => "Viktoria",
    "last_name" => "W.",
    "country" => "Bulgaria",
    "continent" => "Europe",
    "age" => 98,
    "language" => "PHP"
  ],
  [
    "first_name" => "Piotr",
    "last_name" => "B.",
    "country" => "Poland",
    "continent" => "Europe",
    "age" => 128,
    "language" => "JavaScript"
  ]
];
```

```python
list1 = [
  { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 19, 'language': 'Python' },
  { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 29, 'language': 'JavaScript' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
  { 'firstName': 'Noa', 'lastName': 'A.', 'country': 'Israel', 'continent': 'Asia', 'age': 40, 'language': 'Ruby' },
  { 'firstName': 'Andrei', 'lastName': 'E.', 'country': 'Romania', 'continent': 'Europe', 'age': 59, 'language': 'C' },
  { 'firstName': 'Maria', 'lastName': 'S.', 'country': 'Peru', 'continent': 'Americas', 'age': 60, 'language': 'C' },
  { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 75, 'language': 'Python' },
  { 'firstName': 'Chloe', 'lastName': 'K.', 'country': 'Guernsey', 'continent': 'Europe', 'age': 88, 'language': 'Ruby' },
  { 'firstName': 'Viktoria', 'lastName': 'W.', 'country': 'Bulgaria', 'continent': 'Europe', 'age': 98, 'language': 'PHP' },
  { 'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128, 'language': 'JavaScript' }
]
```
```cobol
       01  List.
          03  ListLength      pic 9(2) value 10.
          03  dev1.
              05 FirstName    pic a(9)  value 'Harry'.
              05 LastName     pic x(2)  value 'K.'.
              05 Country      pic a(24) value 'Brazil'.
              05 Continent    pic a(8)  value 'Americas'.
              05 Age          pic 9(3)  value 19.
              05 Language     pic a(10) value 'Python'.
          03  dev2.
              05 FirstName    pic a(9)  value 'Kseniya'.
              05 LastName     pic x(2)  value 'T.'.
              05 Country      pic a(24) value 'Belarus'.
              05 Continent    pic a(8)  value 'Europe'.
              05 Age          pic 9(3)  value 29.
              05 Language     pic a(10) value 'JavaScript'.
          03  dev3.
              05 FirstName    pic a(9)  value 'Jing'.
              05 LastName     pic x(2)  value 'X.'.
              05 Country      pic a(24) value 'China'.
              05 Continent    pic a(8)  value 'Asia'.
              05 Age          pic 9(3)  value 39.
              05 Language     pic a(10) value 'Ruby'.
          03  dev4.
              05 FirstName    pic a(9)  value 'Noa'.
              05 LastName     pic x(2)  value 'A.'.
              05 Country      pic a(24) value 'Israel'.
              05 Continent    pic a(8)  value 'Asia'.
              05 Age          pic 9(3)  value 40.
              05 Language     pic a(10) value 'Ruby'.
          03  dev5.
              05 FirstName    pic a(9)  value 'Andrei'.
              05 LastName     pic x(2)  value 'E.'.
              05 Country      pic a(24) value 'Romania'.
              05 Continent    pic a(8)  value 'Europe'.
              05 Age          pic 9(3)  value 59.
              05 Language     pic a(10) value 'C'.
          03  dev6.
              05 FirstName    pic a(9)  value 'Maria'.
              05 LastName     pic x(2)  value 'S.'.
              05 Country      pic a(24) value 'Peru'.
              05 Continent    pic a(8)  value 'Americas'.
              05 Age          pic 9(3)  value 60.
              05 Language     pic a(10) value 'C'.
          03  dev7.
              05 FirstName    pic a(9)  value 'Lukas'.
              05 LastName     pic x(2)  value 'X.'.
              05 Country      pic a(24) value 'Croatia'.
              05 Continent    pic a(8)  value 'Europe'.
              05 Age          pic 9(3)  value 75.
              05 Language     pic a(10) value 'Python'.
          03  dev8.
              05 FirstName    pic a(9)  value 'Chloe'.
              05 LastName     pic x(2)  value 'K.'.
              05 Country      pic a(24) value 'Guernsey'.
              05 Continent    pic a(8)  value 'Europe'.
              05 Age          pic 9(3)  value 88.
              05 Language     pic a(10) value 'Ruby'.
          03  dev9.
              05 FirstName    pic a(9)  value 'Viktoria'.
              05 LastName     pic x(2)  value 'W.'.
              05 Country      pic a(24) value 'Bulgaria'.
              05 Continent    pic a(8)  value 'Europe'.
              05 Age          pic 9(3)  value 98.
              05 Language     pic a(10) value 'PHP'.
          03  dev10.
              05 FirstName    pic a(9)  value 'Piotr'.
              05 LastName     pic x(2)  value 'B.'.
              05 Country      pic a(24) value 'Poland'.
              05 Continent    pic a(8)  value 'Europe'.
              05 Age          pic 9(3)  value 128.
              05 Language     pic a(10) value 'JavaScript'.
```

your function should return `true` as there is at least one developer from each age group.

Notes:

 - The input array will always be valid and formatted as in the example above.
 - Age is represented by a number which can be any positive integer up to 199.
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
