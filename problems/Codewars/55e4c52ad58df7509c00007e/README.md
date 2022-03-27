[_metadata_:generated]: - "true"

# Invalid Login - Bug Fixing #11

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`55e4c52ad58df7509c00007e`](https://www.codewars.com/kata/55e4c52ad58df7509c00007e) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

# Invalid Login - Bug Fixing #11

Oh NO! Timmy has moved divisions... but now he's in the field of security. Timmy, being the top coder he is, has allowed some bad code through. You must help Timmy and filter out any injected code!

## Task

Your task is simple, search the password string for any injected code (Injected code is any thing that would be used to exploit flaws in the current code, so basically anything that contains `||` or `//`) if you find any you must return `"Wrong username or password!"` because no one likes someone trying to cheat their way in!


## Preloaded

You will be given a preloaded class called `Database` with a method `login` this takes two parameters `username` and `password`. This is a generic login function which will check the database for the user it will return either `'Successfully Logged in!'` if it passes the test or `'Wrong username or password!'` if either the password is wrong or username does not exist.


## Usage

```javascript
var database = new Database();
database.login('Timmy', 'password');
```
```python
database = Database()
database.login('Timmy', 'password')
```
```ruby
database = Database.new;
database.login('Timmy', 'password')
```
