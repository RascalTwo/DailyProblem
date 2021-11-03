# Lowest-Weight Path in K connections

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

You are given a huge list of airline ticket prices between different cities around the world on a given day.

These are all direct flights. Each element in the list has the format `(source_city, destination, price)`.

Consider a user who is willing to take up to `k` connections from their origin city `A` to their destination `B`.

Find the cheapest fare possible for this journey and print the itinerary for that journey.

For example, our traveler wants to go from `JFK` to `LAX` with up to `3` connections, and our input flights are as follows:

    [
        ('JFK', 'ATL', 150),
        ('ATL', 'SFO', 400),
        ('ORD', 'LAX', 200),
        ('LAX', 'DFW', 80),
        ('JFK', 'HKG', 800),
        ('ATL', 'ORD', 90),
        ('JFK', 'LAX', 500),
    ]

Due to some improbably low flight prices, the cheapest itinerary would be `JFK -> ATL -> ORD -> LAX`, costing `$440`.

## Examples

| Input                                                                                                                                                                                                                                                                                                      | Output                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| <table><tr><th>connections</th><th>start</th><th>destionation</th><th>hops</th></tr><tr><td>`[('JFK', 'ATL', 150), ('ATL', 'SFO', 400), ('ORD', 'LAX', 200), ('LAX', 'DFW', 80), ('JFK', 'HKG', 800), ('ATL', 'ORD', 90), ('JFK', 'LAX', 500)]`</td><td>`JFK`</td><td>`LAX`</td><td>`3`</td></tr></table>  | `['JFK', 'ATL', 'ORD', 'LAX']` |
| <table><tr><th>connections</th><th>start</th><th>destionation</th><th>hops</th></tr><tr><td>`[('JFK', 'ATL', 1500), ('ATL', 'SFO', 400), ('ORD', 'LAX', 200), ('LAX', 'DFW', 80), ('JFK', 'HKG', 800), ('ATL', 'ORD', 90), ('JFK', 'LAX', 500)]`</td><td>`JFK`</td><td>`LAX`</td><td>`3`</td></tr></table> | `['JFK', 'LAX']`               |
