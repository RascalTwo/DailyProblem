[_metadata_:generated]: - "true"

# Coding Meetup #8 - Higher-Order Functions Series - Will all continents be represented?

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`58291fea7ff3f640980000f9`](https://www.codewars.com/kata/58291fea7ff3f640980000f9) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You will be given a sequence of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next coding meetup that you are organising.

Your task is to return:

- `true` if all of the following continents / geographic zones will be represented by at least one developer: 'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'.
- `false` otherwise.

For example, given the following input array:

```javascript
var list1 = [
  { firstName: 'Fatima', lastName: 'A.', country: 'Algeria', continent: 'Africa', age: 25, language: 'JavaScript' },
  { firstName: 'Agustín', lastName: 'M.', country: 'Chile', continent: 'Americas', age: 37, language: 'C' },
  { firstName: 'Jing', lastName: 'X.', country: 'China', continent: 'Asia', age: 39, language: 'Ruby' },
  { firstName: 'Laia', lastName: 'P.', country: 'Andorra', continent: 'Europe', age: 55, language: 'Ruby' },
  { firstName: 'Oliver', lastName: 'Q.', country: 'Australia', continent: 'Oceania', age: 65, language: 'PHP' },
];
```
```php
$list1 = [
  [
    "first_name" => "Fatima",
    "last_name" => "A.",
    "country" => "Algeria",
    "continent" => "Africa",
    "age" => 25,
    "language" => "JavaScript"
  ],
  [
    "first_name" => "Agustin",
    "last_name" => "M.",
    "country" => "Chile",
    "continent" => "Americas",
    "age" => 37,
    "language" => "C"
  ],
  [
    "first_name" => "Jing",
    "last_name" => "X",
    "country" => "China",
    "continent" => "Asia",
    "age" => 39,
    "language" => "Ruby"
  ],
  [
    "first_name" => "Laia",
    "last_name" => "P.",
    "country" => "Andorra",
    "continent" => "Europe",
    "age" => 55,
    "language" => "Ruby"
  ],
  [
    "first_name" => "Oliver",
    "last_name" => "Q.",
    "country" => "Australia",
    "continent" => "Oceania",
    "age" => 65,
    "language" => "PHP"
  ]
];
```

```python
list1 =  [
  { 'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript' },
  { 'firstName': 'Agustín', 'lastName': 'M.', 'country': 'Chile', 'continent': 'Americas', 'age': 37, 'language': 'C' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
  { 'firstName': 'Laia', 'lastName': 'P.', 'country': 'Andorra', 'continent': 'Europe', 'age': 55, 'language': 'Ruby' },
  { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 65, 'language': 'PHP' }
  ]
```
```cobol
       01  List.
          03  ListLength      pic 9(2) value 5.
          03  dev1.
              05 FirstName    pic a(9)  value 'Fatima'.
              05 LastName     pic x(2)  value 'A.'.
              05 Country      pic a(24) value 'Algeria'.
              05 Continent    pic a(8)  value 'Africa'.
              05 Age          pic 9(3)  value 25.
              05 Language     pic a(10) value 'JavaScript'.
          03  dev2.
              05 FirstName    pic a(9)  value 'Agustin'.
              05 LastName     pic x(2)  value 'M.'.
              05 Country      pic a(24) value 'Chile'.
              05 Continent    pic a(8)  value 'Americas'.
              05 Age          pic 9(3)  value 37.
              05 Language     pic a(10) value 'C'.
          03  dev3.
              05 FirstName    pic a(9)  value 'Jing'.
              05 LastName     pic x(2)  value 'X.'.
              05 Country      pic a(24) value 'China'.
              05 Continent    pic a(8)  value 'Asia'.
              05 Age          pic 9(3)  value 39.
              05 Language     pic a(10) value 'Ruby'.
          03  dev4.
              05 FirstName    pic a(9)  value 'Laia'.
              05 LastName     pic x(2)  value 'P.'.
              05 Country      pic a(24) value 'Andorra'.
              05 Continent    pic a(8)  value 'Europe'.
              05 Age          pic 9(3)  value 55.
              05 Language     pic a(10) value 'Ruby'.
          03  dev5.
              05 FirstName    pic a(9)  value 'Oliver'.
              05 LastName     pic x(2)  value 'Q.'.
              05 Country      pic a(24) value 'Australia'.
              05 Continent    pic a(8)  value 'Oceania'.
              05 Age          pic 9(3)  value 69.
              05 Language     pic a(10) value 'PHP'.
```

your function should return `true` as there is at least one developer from the required 5 geographic zones.

Notes:

 - The input array and continent names will always be valid and formatted as in the list above for example 'Africa' will always start with upper-case 'A'.
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
