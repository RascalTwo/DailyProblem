[_metadata_:generated]: - "true"

# SQL: Concatenating Columns

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                     |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`59440034e94fae05b2000073`](https://www.codewars.com/kata/59440034e94fae05b2000073) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924086/postgresql_pzymmo.svg" alt="PostgreSQL" title="PostgreSQL" width="50" />](solve.sql) |

<!-- INFO TABLE END -->

Given the table below:

** names table schema **
* id
* prefix
* first
* last
* suffix

Your task is to use a select statement to return a single column table containing the full title of the person (concatenate all columns together except id), as follows:

** output table schema **
* title

Don't forget to add spaces.
