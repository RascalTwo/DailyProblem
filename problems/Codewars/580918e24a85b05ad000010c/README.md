[_metadata_:generated]: - "true"

# SQL Basics: Simple JOIN with COUNT

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                     |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`580918e24a85b05ad000010c`](https://www.codewars.com/kata/580918e24a85b05ad000010c) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924086/postgresql_pzymmo.svg" alt="PostgreSQL" title="PostgreSQL" width="50" />](solve.sql) |

<!-- INFO TABLE END -->

For this challenge you need to create a simple SELECT statement that will return all columns from the `people` table, and join to the `toys` table so that you can return the COUNT of the toys

### people table schema
- id
- name

### toys table schema
- id
- name
- people_id

You should return all people fields as well as the toy count as "toy_count".

> NOTE: You're solution should use pure SQL. Ruby is used within the test cases to do the actual testing.
