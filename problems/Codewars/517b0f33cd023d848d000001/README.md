[_metadata_:generated]: - "true"

# Ninja vs Samurai: Strike

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`517b0f33cd023d848d000001`](https://www.codewars.com/kata/517b0f33cd023d848d000001) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924063/c_bnvpsm.svg" alt="C#" title="C#" width="50" />](solve.cs)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924090/ruby_v4klwh.svg" alt="Ruby" title="Ruby" width="50" />](solve.rb) |

<!-- INFO TABLE END -->

Something is wrong with our Warrior class. The strike method does not work correctly. The following shows an example of this code being used:

```javascript
var ninja = new Warrior('Ninja');
var samurai = new Warrior('Samurai');

samurai.strike(ninja, 3);
// ninja.health should == 70
```
```typescript
var ninja = new Warrior('Ninja');
var samurai = new Warrior('Samurai');

samurai.strike(ninja, 3);
// ninja.health should == 70
```
```coffeescript
ninja = new Warrior('Ninja')
samurai = new Warrior('Samurai')

samurai.strike(ninja, 3)
# ninja.health should == 70
```
```python
ninja = Warrior('Ninja')
samurai = Warrior('Samurai')

samurai.strike(ninja, 3)
# ninja.health should == 70
```
```ruby
ninja = Warrior.new('Ninja')
samurai = Warrior.new('Samurai')

samurai.strike(ninja, 3)
# ninja.health should == 70
```
```csharp
var ninja = new Warrior("Ninja");
var samurai = new Warrior("Samurai");

samurai.Strike(ninja, 3);
// ninja.Health should == 70
```

Can you figure out what is wrong?

