[_metadata_:generated]: - "true"

# SQL Basics: Simple GROUP BY

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                     |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`58111f4ee10b5301a7000175`](https://www.codewars.com/kata/58111f4ee10b5301a7000175) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924086/postgresql_pzymmo.svg" alt="PostgreSQL" title="PostgreSQL" width="50" />](solve.sql) |

<!-- INFO TABLE END -->

For this challenge you need to create a simple GROUP BY statement, you want to group all the people by their age and count the people who have the same age.

### people table schema
- id
- name
- age

### select table schema
- age [group by]
- people_count (people count)


> NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.