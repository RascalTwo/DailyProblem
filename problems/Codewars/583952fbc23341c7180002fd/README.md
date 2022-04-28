[_metadata_:generated]: - "true"

# Coding Meetup #14 - Higher-Order Functions Series - Order the food

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`583952fbc23341c7180002fd`](https://www.codewars.com/kata/583952fbc23341c7180002fd) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You will be given an array of objects representing data about developers who have signed up to attend the next coding meetup that you are organising.

Your task is to return an **object which includes the count of food options selected by the developers on the meetup sign-up form.**.

For example, given the following input array:

```javascript
var list1 = [
  { firstName: 'Noah', lastName: 'M.', country: 'Switzerland', continent: 'Europe', age: 19, language: 'C', 
    meal: 'vegetarian' },
  { firstName: 'Anna', lastName: 'R.', country: 'Liechtenstein', continent: 'Europe', age: 52, language: 'JavaScript', 
    meal: 'standard' },
  { firstName: 'Ramona', lastName: 'R.', country: 'Paraguay', continent: 'Americas', age: 29, language: 'Ruby', 
    meal: 'vegan' },
  { firstName: 'George', lastName: 'B.', country: 'England', continent: 'Europe', age: 81, language: 'C', 
    meal: 'vegetarian' },
];
```

```python
list1 = [
    { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C', 'meal': 'vegetarian' },
    { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript', 'meal': 'standard' },
    { 'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby', 'meal': 'vegan' },
    { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C', 'meal': 'vegetarian' },
]
```
```cobol
       01  List.
          03  ListLength      pic 9(2) value 4.
          03  dev1.
              05 FirstName    pic a(9)   value 'Noah'.
              05 LastName     pic x(2)   value 'M.'.
              05 Country      pic a(24)  value 'Switzerland'.
              05 Continent    pic a(8)   value 'Europe'.
              05 Age          pic 9(3)   value 19.
              05 Language     pic a(10)  value 'C'.
              05 Meal         pic a(17)  value 'vegetarian'.
          03  dev2.
              05 FirstName    pic a(9)   value 'Anna'.
              05 LastName     pic x(2)   value 'R.'.
              05 Country      pic a(24)  value 'Liechtenstein'.
              05 Continent    pic a(8)   value 'Europe'.
              05 Age          pic 9(3)   value 52.
              05 Language     pic a(10)  value 'JavaScript'.
              05 Meal         pic a(17)  value 'standard'.
          03  dev3.
              05 FirstName    pic a(9)   value 'Ramona'.
              05 LastName     pic x(2)   value 'R.'.
              05 Country      pic a(24)  value 'Paraguay'.
              05 Continent    pic a(8)   value 'Americas'.
              05 Age          pic 9(3)   value 29.
              05 Language     pic a(10)  value 'Ruby'.
              05 Meal         pic a(17)  value 'vegan'.
          03  dev4.
              05 FirstName    pic a(9)   value 'George'.
              05 LastName     pic x(2)   value 'B.'.
              05 Country      pic a(24)  value 'England'.
              05 Continent    pic a(8)   value 'Europe'.
              05 Age          pic 9(3)   value 81.
              05 Language     pic a(10)  value 'C'.
              05 Meal         pic a(17)  value 'vegetarian'.
```

your function should return the following object (the order of properties does not matter):

```javascript
{ vegetarian: 2, standard: 1, vegan: 1 }
```

```python
{ 'vegetarian': 2, 'standard': 1, 'vegan': 1 }
```

```cobol
        [['vegetarian', 2], ['standard', 1], ['vegan', 1]]      
```

Notes:

 - The order of the meals count in the object does not matter. 
 - The count value should be a valid number.
 - The input array will always be valid and formatted as in the example above.
 - there are 5 possible meal options and the strings representing the selected meal option will always be formatted in the same way, as follows: `'standard'`,  `'vegetarian'`, `'vegan'`, `'diabetic'`, `'gluten-intolerant'`.
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
