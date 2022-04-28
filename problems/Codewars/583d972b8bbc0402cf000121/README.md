[_metadata_:generated]: - "true"

# Coding Meetup #16 - Higher-Order Functions Series - Ask for missing details

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`583d972b8bbc0402cf000121`](https://www.codewars.com/kata/583d972b8bbc0402cf000121) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

You will be given an array of objects representing data about developers who have signed up to attend the next coding meetup that you are organising.

Given the following input array:

```javascript
var list1 = [
  { firstName: null, lastName: 'I.', country: 'Argentina', continent: 'Americas', age: 35, language: 'Java' },
  { firstName: 'Lukas', lastName: 'X.', country: 'Croatia', continent: 'Europe', age: 35, language: null },
  { firstName: 'Madison', lastName: 'U.', country: 'United States', continent: 'Americas', age: 32, language: 'Ruby' } 
];
```
```cobol
       01  List.
          03  ListLength      pic 9(2) value 3.
          03  dev1.
              05 FirstName    pic a(9).
              05 LastName     pic x(2)  value 'I.'.
              05 Country      pic a(24) value 'Argentina'.
              05 Continent    pic a(8)  value 'Americas'.
              05 Age          pic 9(3)  value 35.
              05 Language     pic a(10) value 'Java'.
          03  dev2.
              05 FirstName    pic a(9)  value 'Lukas'.
              05 LastName     pic x(2)  value 'X.'.
              05 Country      pic a(24) value 'Croatia'.
              05 Continent    pic a(8)  value 'Europe'.
              05 Age          pic 9(3)  value 35.
              05 Language     pic a(10).
          03  dev3.
              05 FirstName    pic a(9)  value 'Madison'.
              05 LastName     pic x(2)  value 'U.'.
              05 Country      pic a(24) 
                              value 'United States of America'.
              05 Continent    pic a(8)  value 'Americas'.
              05 Age          pic 9(3)  value 32.
              05 Language     pic a(10) value 'Ruby'.
```

write a function that

1) adds the `question` property to each object in the input array where the developer has not provided the relevant details (marked with a `null` value in JavaScript, with the default value in COBOL). The value of the `question` property should be the following string:

`Hi, could you please provide your <property name>.`


2) and returns only the developers with missing details:


```javascript
[
  { firstName: null, lastName: 'I.', country: 'Argentina', continent: 'Americas', age: 35, language: 'Java', 
  question: 'Hi, could you please provide your firstName.' },
  { firstName: 'Lukas', lastName: 'X.', country: 'Croatia', continent: 'Europe', age: 35, language: null, 
  question: 'Hi, could you please provide your language.' }
]
```
```cobol
       01  result.
          03  ResLength       pic 9(2) value 2.
          03  .
              05 FirstName    pic a(9).
              05 LastName     pic x(2)  value 'I.'.
              05 Country      pic a(24) value 'Argentina'.
              05 Continent    pic a(8)  value 'Americas'.
              05 Age          pic 9(3)  value 35.
              05 Language     pic a(10) value 'Java'.
              05 Question     pic x(43) 
                 value 'Hi, could you please provide your FirstName.'.
          03  .
              05 FirstName    pic a(9)  value 'Lukas'.
              05 LastName     pic x(2)  value 'X.'.
              05 Country      pic a(24) value 'Croatia'.
              05 Continent    pic a(8)  value 'Europe'.
              05 Age          pic 9(3)  value 35.
              05 Language     pic x(10).
              05 Question     pic x(44) 
                 value 'Hi, could you please provide your Language.'.
```




Notes:

 - At most only one of the values will be `null` / empty.
 - Preserve the order of the original list.
 - Return an empty array `[]` if there is no developer with missing details.
 - The input array will always be valid and formatted as in the example above.
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

<a href="https://www.codewars.com/kata/coding-meetup-number-17-higher-order-functions-series-sort-by-programming-language">Coding Meetup #17 - Higher-Order Functions Series - Sort by programming language</a>
