# Courier Active Time Calculator

<!-- INFO TABLE BEGIN -->

| Provider                                              | Solutions                                                                                                                                        |
| :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: |
| [DailyCoding](../../../docs/providers/DailyCoding.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py) |

<!-- INFO TABLE END -->

The “active time” of a courier is the time between the pickup and dropoff of a delivery.

Given a set of data formatted like the following: `(delivery id, timestamp, pickup/dropoff)`

Calculate the total active time in seconds.

> A courier can pick up multiple orders before dropping them off.

## Examples

If the input is the following:

    (1, 1570320047, 'pickup' )
    (1, 1570320725, 'dropoff')
    (2, 1570321092, 'pickup' )
    (3, 1570321212, 'pickup' )
    (3, 1570322352, 'dropoff')
    (2, 1570323012, 'dropoff')

The total active time would be `3738` seconds.
