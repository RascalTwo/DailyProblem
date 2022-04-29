[_metadata_:generated]: - "true"

# The Office II - Boredom Score

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`57ed4cef7b45ef8774000014`](https://www.codewars.com/kata/57ed4cef7b45ef8774000014) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Every now and then people in the office moves teams or departments. Depending what people are doing with their time they can become more or less boring. Time to assess the current team.

```if-not:java
You will be provided with an object(staff) containing the staff names as keys, and the department they work in as values.
```

```if:java
You will be provided with an array of `Person` objects with each instance containing the name and department for a staff member.
~~~java
public class Person {
  public final String name;        // name of the staff member
  public final String department;  // department they work in
}
~~~
```

Each department has a different boredom assessment score, as follows:

accounts = 1<br>
finance = 2 <br>
canteen = 10 <br>
regulation = 3 <br>
trading = 6 <br>
change = 6<br>
IS = 8<br>
retail = 5<br> 
cleaning = 4<br>
pissing about = 25<br>

Depending on the cumulative score of the team, return the appropriate sentiment:

<=80: 'kill me now'<br>
< 100 & > 80: 'i can handle this'<br>
100 or over: 'party time!!'

<a href='https://www.codewars.com/kata/the-office-i-outed'>The Office I - Outed</a><br>
<a href='https://www.codewars.com/kata/the-office-iii-broken-photocopier'>The Office III - Broken Photocopier</a><br>
<a href='https://www.codewars.com/kata/the-office-iv-find-a-meeting-room'>The Office IV - Find a Meeting Room</a><br>
<a href='https://www.codewars.com/kata/the-office-v-find-a-chair'>The Office V - Find a Chair</a><br>
