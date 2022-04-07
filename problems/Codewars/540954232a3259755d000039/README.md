[_metadata_:generated]: - "true"

# Friday the 13ths

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`540954232a3259755d000039`](https://www.codewars.com/kata/540954232a3259755d000039) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Create the function `fridayTheThirteenths` that accepts a `start` year and an `end` year (*inclusive*), and returns all of the dates where the 13th of a month lands on a Friday in the given range of year(s).

The return value should be a string where each date is *seperated by a space*.  The date should be formatted like `9/13/2014` where months do *not* have leading zeroes and are separated with forward slashes.

If no `end` year is given, only return friday the thirteenths during the `start` year.

## Examples
```javascript
fridayTheThirteenths(1999, 2000) 
  // returns "8/13/1999 10/13/2000"
  
fridayTheThirteenths(2014, 2015) 
  // returns "6/13/2014 2/13/2015 3/13/2015 11/13/2015"
  
fridayTheThirteenths(2000)
  // returns "10/13/2000"
```
```coffeescript
fridayTheThirteenths 1999, 2000
  # returns "8/13/1999 10/13/2000"

fridayTheThirteenths 2014, 2015
  # returns "6/13/2014 2/13/2015 3/13/2015 11/13/2015"

fridayTheThirteenths 2000
  # returns "10/13/2000"
```
```csharp
Kata.FridayTheThirteenths(1999, 2000)
  # returns "8/13/1999 10/13/2000"

Kata.FridayTheThirteenths(2014, 2015)
  # returns "6/13/2014 2/13/2015 3/13/2015 11/13/2015"

Kata.FridayTheThirteenths(2000)
  # returns "10/13/2000"
```
```cobol
      FridayTheThirteenths(1999, 2000)
      => result = "8/13/1999 10/13/2000"

      FridayTheThirteenths(2014, 2015)
      => result = "6/13/2014 2/13/2015 3/13/2015 11/13/2015"

      FridayTheThirteenths(2000, 0000)
      => returns = "10/13/2000"
```

This kata was designed to use the built-in `Date` object.  Dates can often be finicky, so while there are other methods to get the correct dates, I can't guarantee they will work.
