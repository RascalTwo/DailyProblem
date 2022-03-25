[_metadata_:generated]: - "true"

# "this" is a problem 

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`547c71fdc5b2b38db1000098`](https://www.codewars.com/kata/547c71fdc5b2b38db1000098) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

We want to create a constructor function 'NameMe', which takes first name and last name as parameters. The function combines the first and last names and saves the value in "name" property.

We already implemented that function, but when we actually run the code, the "name" property is accessible, but the "firstName" and "lastName" is not accessible. All the properties should be accessible. Can you find what's wrong with it?
A test fixture is also available
```javascript
function NameMe(first, last) {
    this.firstName = first;
    this.lastName = last;
    return {name: this.firstName + ' ' + this.lastName};
}

var n = new NameMe('John', 'Doe');
n.firstName //Expected: John
n.lastName //Expected: Doe
n.name //Expected: John Doe

```

```java
public class NameMe {
    private String firstName;
    private String lastName;
    private String fullName;

    public NameMe(String first, String last) {
        this.firstName = first;
        this.lastName = last;
   }
 }

NameMe nameMe = new NameMe("John", "Doe");
nameMe.getFirstName(); //Expected: John
nameMe.getLastName(); //Expected: Doe
nameMe.getFullName(); //Expected: John Doe


```
