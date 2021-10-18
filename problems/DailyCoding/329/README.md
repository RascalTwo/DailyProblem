# Stable Marriage

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

The stable marriage problem is defined as follows:

Suppose you have `N` men and `N` women, and each person has ranked their prospective opposite-sex partners in order of preference.

For example, if `N = 3`, the input could be something like this:

```python
guy_preferences = {
    'andrew': ['caroline', 'abigail', 'betty'],
    'bill': ['caroline', 'betty', 'abigail'],
    'chester': ['betty', 'caroline', 'abigail'],
}

gal_preferences = {
    'abigail': ['andrew', 'bill', 'chester'],
    'betty': ['bill', 'andrew', 'chester'],
    'caroline': ['bill', 'chester', 'andrew']
}
```

Write an algorithm that pairs the men and women together in such a way that no two people of opposite sex would both rather be with each other than with their current partners.

## Examples

| Input                                                                                                                                                                                                                                                                                                                                                                   | Output                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| <table><tr><th>guy_preferences</th><th>gal_preferences</th></tr><tr><td>`{'andrew': ['caroline', 'abigail', 'betty'], 'bill': ['caroline', 'betty', 'abigail'], 'chester': ['betty', 'caroline', 'abigail']}`</td><td>`{'abigail': ['andrew', 'bill', 'chester'], 'betty': ['bill', 'andrew', 'chester'], 'caroline': ['bill', 'chester', 'andrew']}`</td></tr></table> | `{ 'bill': 'caroline', 'andrew': 'abigail', 'chester': 'betty'}` |
