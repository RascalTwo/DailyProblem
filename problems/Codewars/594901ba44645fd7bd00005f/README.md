[_metadata_:generated]: - "true"

# SQL Basics: Maths with String Manipulations

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                     |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`594901ba44645fd7bd00005f`](https://www.codewars.com/kata/594901ba44645fd7bd00005f) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924086/postgresql_pzymmo.svg" alt="PostgreSQL" title="PostgreSQL" width="50" />](solve.sql) |

<!-- INFO TABLE END -->

Given a demographics table in the following format:

### demographics table schema

* id
* name
* birthday
* race

return a single column named `calculation` where the value is the bit length of name, added to the number of characters in race.
