[_metadata_:number]:-      "132"
[_metadata_:difficulty]:-  "Easy"
[_metadata_:asker]:-       "Riot Games"
[_metadata_:tags]:-        "data-structure"

# 132

Design and implement a HitCounter class that keeps track of requests (or hits).
It should support the following operations:

- `record(timestamp)`
  - records a hit that happened at timestamp
- `total()`
  -  returns the total number of hits recorded
- `range(lower, upper)`
  - returns the number of hits that occurred between timestamps lower and upper (inclusive)

Follow-up: What if our system has limited memory?