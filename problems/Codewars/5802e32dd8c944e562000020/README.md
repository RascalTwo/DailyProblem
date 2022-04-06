[_metadata_:generated]: - "true"

# SQL Basics: Simple JOIN

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                     |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5802e32dd8c944e562000020`](https://www.codewars.com/kata/5802e32dd8c944e562000020) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924086/postgresql_pzymmo.svg" alt="PostgreSQL" title="PostgreSQL" width="50" />](solve.sql) |

<!-- INFO TABLE END -->

For this challenge you need to create a simple SELECT statement that will return all columns from the `products` table, and join to the `companies` table so that you can return the company name. 

### products table schema
- id
- name
- isbn
- company_id
- price

### companies table schema
- id
- name

You should return all product fields as well as the company name as "company_name".

> NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.
