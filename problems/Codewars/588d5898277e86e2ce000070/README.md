[_metadata_:generated]: - "true"

# JSON Account Updater

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`588d5898277e86e2ce000070`](https://www.codewars.com/kata/588d5898277e86e2ce000070) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

A system is receiving each hour a batch with logon information.  
Can you write a method that can update accounts with the latest logon data? 

### Task

Finish this function:
```javascript
function updateAccounts(accounts, logons) {}
```

The function accepts `"Accounts"` and returns the same list updated. The list of accounts is a JSON object:

```javascript
var accounts = {
  "Accounts": [
    {
      "Id": 21,
      "Name": "John Shepherd",
      "LogonCount" : 13,
      "LastLogon" : new Date(2017, 1, 14, 16, 15, 6, 111)
    },
    {
      // ...
    }
  ]
}
```

The function accepts a list of `"Logons"` that is a JSON object:

```javascript
var logons = {
  "Logons": [
    {
      "Id": 21,
      "Name": "John Shepherd",
      "Date" : new Date(2017, 1, 14, 16, 15, 6, 111)
    },
    {
      // ...
    }
  ]
}
```

The updates must follow this pattern:

* Accounts are matched with the logon information by the `"Id"` fields.
* If an account matches a logon, The `"LogonCount"` is incremented with 1.
* If `"Id"` is not found, a new account will be added with all available information where `"LogonCount"` is set to 1.
* If `"LastLogon"` is older than the logon `"Date"` it will be set to the logon `"Date"`.
* If `"LastLogon"` is older than the logon `"Date"` the `"Name"` will be set to the logon `"Name"` when not empty.
* Accounts are returned ordered by `"Id"` ascending, but they are not necessarily ordered when they are passed as a parameter.
