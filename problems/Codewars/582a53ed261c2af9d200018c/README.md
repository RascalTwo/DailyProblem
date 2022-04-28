[_metadata_:generated]: - "true"

# Coding Meetup #10 - Higher-Order Functions Series - Create usernames

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`582a53ed261c2af9d200018c`](https://www.codewars.com/kata/582a53ed261c2af9d200018c) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Given the following input array:

```javascript
var list1 = [
  { firstName: 'Emily', lastName: 'N.', country: 'Ireland', continent: 'Europe', age: 30, language: 'Ruby' },
  { firstName: 'Nor', lastName: 'E.', country: 'Malaysia', continent: 'Asia', age: 20, language: 'Clojure' }
];
```
```cobol
       01  List.
          03  ListLength      pic 9(2) value 2.
          03  dev1.
              05 FirstName    pic a(9)  value 'Emily'.
              05 LastName     pic x(2)  value 'N.'.
              05 Country      pic a(24) value 'Ireland'.
              05 Continent    pic a(8)  value 'Europe'.
              05 Age          pic 9(3)  value 98.
              05 Language     pic a(10) value 'Ruby'.
          03  dev2.
              05 FirstName    pic a(9)  value 'Nor'.
              05 LastName     pic x(2)  value 'E.'.
              05 Country      pic a(24) value 'Malaysia'.
              05 Continent    pic a(8)  value 'Asia'.
              05 Age          pic 9(3)  value 21.
              05 Language     pic a(10) value 'Clojure'.
```

write a function that adds the `username` property to each object in the input array:

```javascript
[
  { firstName: 'Emily', lastName: 'N.', country: 'Ireland', continent: 'Europe', age: 30, language: 'Ruby', 
    username: 'emilyn1990' },
  { firstName: 'Nor', lastName: 'E.', country: 'Malaysia', continent: 'Asia', age: 20, language: 'Clojure', 
    username: 'nore2000' }
]
```
```cobol
       01  result.
          03  ResLength       pic 9(2) value 2.
          03  dev1.
              05 FirstName    pic a(9)  value 'Emily'.
              05 LastName     pic x(2)  value 'N.'.
              05 Country      pic a(24) value 'Ireland'.
              05 Continent    pic a(8)  value 'Europe'.
              05 Age          pic 9(3)  value 98.
              05 Language     pic a(10) value 'Ruby'.
              05 UserName     pic x(14) value 'emilyn1990'.
          03  dev2.
              05 FirstName    pic a(9)  value 'Nor'.
              05 LastName     pic x(2)  value 'E.'.
              05 Country      pic a(24) value 'Malaysia'.
              05 Continent    pic a(8)  value 'Asia'.
              05 Age          pic 9(3)  value 21.
              05 Language     pic a(10) value 'Clojure'.
              05 UserName     pic x(14) value 'nore2000'.
```

The value of the `username` property is composed by concatenating:

- `firstName` in lower-case;
- first letter of the `lastName` in lower-case; and 
- the birth year which for the purpose of this kata is calculated simply by subtracting `age` from the current year. **Please make sure that your function delivers the correct birth year irrespective of when it will be executed, for example it should also work correctly for a meetup organised in 10-years-time.** The example above assumes that the function is run in year 2020.


Notes:

 - The input array will always be valid and formatted as in the example above.
 - Age is represented by a number which can be any positive integer.
 - Lastname will always be one upper-cased letter followed by dot, e.g. `'N.'`
 - Order of the objects in the array should be maintained but order of the properties in the individual objects does not matter.
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
