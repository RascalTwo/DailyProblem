[_metadata_:generated]: - "true"

# SQL Basics: Repeat and Reverse

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                     |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`59414360f5c3947364000070`](https://www.codewars.com/kata/59414360f5c3947364000070) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924086/postgresql_pzymmo.svg" alt="PostgreSQL" title="PostgreSQL" width="50" />](solve.sql) |

<!-- INFO TABLE END -->

Using our monsters table with the following schema:

**monsters table schema**
* id
* name
* legs 
* arms
* characteristics

return the following table:

** output schema**
* name
* characteristics

Where the name is the original string repeated three times (do not add any spaces), and the characteristics are the original strings in reverse (e.g. 'abc, def, ghi' becomes 'ihg ,fed ,cba').
