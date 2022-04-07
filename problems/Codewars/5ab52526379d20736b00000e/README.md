[_metadata_:generated]: - "true"

# Help the Elite Squad of Brazilian forces BOPE

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5ab52526379d20736b00000e`](https://www.codewars.com/kata/5ab52526379d20736b00000e) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

The BOPE is the squad of special forces of police that usually handles the operations in the Favelas in Rio de Janeiro.

In this Kata you have to write a function that determine the number of magazines that every soldier has to have in his bag.
 
You will receive the weapon and the number of streets that they have to cross.
Considering that every street the officer shoots 3 times. Bellow there is the relation of weapons:


PT92 - 17 bullets </br>
M4A1 - 30 bullets </br>
M16A2 - 30 bullets </br>
PSG1 - 5 bullets </br>

Example:

["PT92", 6] => 2 (6 streets 3 bullets each) </br>
["M4A1", 6] => 1

The return Will always be an integer so as the params.

~~~if:fortran
*NOTE: In Fortran the weapon and number of streets are passed in as two separater arguments (the first one a string, the second an integer) instead of a single array.*
~~~

~~~if:c
*NOTE: In C the weapon and number of streets are passed in as two separate arguments (the first one a string, the second an integer) instead of a single array.*
~~~
