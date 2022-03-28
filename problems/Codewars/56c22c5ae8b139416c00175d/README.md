[_metadata_:generated]: - "true"

# Job Matching #1

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`56c22c5ae8b139416c00175d`](https://www.codewars.com/kata/56c22c5ae8b139416c00175d) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Let's build a matchmaking system that helps discover jobs for developers based on a number of factors.

One of the simplest, yet most important factors is compensation. As developers we know how much money we need to support our lifestyle, so we generally have a rough idea of the minimum salary we would be satisfied with. 

Let's give this a try. We'll create a function `match` which takes a `candidate` and a `job`, which will return a boolean indicating whether the job is a valid match for the candidate. 

A candidate will have a minimum salary, so it will look like this:

```javascript
let candidate = {
  minSalary: 120000
}
```
```ruby
candidate = {
  'min_salary': 120000
}
```
```python
candidate = {
  'min_salary': 120000
}
```
```csharp
Candidate candidate = 
  new Candidate(MinSalary: 120000);
```

A job will have a maximum salary, so it will look like this: 

```javascript 
let job = {
  maxSalary: 140000
}
```
```ruby
job = { 
  'max_salary': 140000
}
```
```python
job = {
  'max_salary': 140000
}
```
```csharp
Job job = 
  new Job(MaxSalary: 140000);
```

If either the candidate's minimum salary or the job's maximum salary is not present, throw an error. 

For a valid match, the candidate's minimum salary must be less than or equal to the job's maximum salary. However, let's also include 10% wiggle room (deducted from the candidate's minimum salary) in case the candidate is a rockstar who enjoys programming on Codewars in their spare time. The company offering the job may be able to work something out. 

---

Continue on with Kata:

- [Job Matching #2][3]
- [Job Matching #3][2]

[3]:https://www.codewars.com/kata/56c2578be8b139bd5c001bd8
[2]:https://www.codewars.com/kata/56c2a067585d9ac8280003c9
