[_metadata_:generated]: - "true"

# SQL Basics - Position

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                     |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`59401e0e54a655a298000040`](https://www.codewars.com/kata/59401e0e54a655a298000040) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924086/postgresql_pzymmo.svg" alt="PostgreSQL" title="PostgreSQL" width="50" />](solve.sql) |

<!-- INFO TABLE END -->

You have access to a table of monsters as follows:

**monsters schema**
* id
* name
* legs
* arms
* characteristics

In each row, the characteristic column has a single comma. Your job is to find it using position(). You must return a table with the format as follows:

**output schema**
* id
* name
* comma

The comma column will contain the position of the comma within the characteristics string. Order the results by comma.

