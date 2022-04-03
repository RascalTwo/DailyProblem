[_metadata_:generated]: - "true"

# Ninja vs Samurai: Attack + Block

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`517b2bcf8557c200b8000015`](https://www.codewars.com/kata/517b2bcf8557c200b8000015) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Something is wrong with our Warrior class. All variables should initialize properly and the attack method is not working as expected.

If properly set, it should correctly calculate the damage after an attack (if the attacker position is == to the block position of the defender: no damage; otherwise, the defender gets 10 damage if hit "high" or 5 damage if hit "low". If no block is set, the defender takes 5 **extra** damage.

For some reason, the health value is not being properly set. The following shows an example of this code being used:

```javascript
var ninja = new Warrior('Ninja');
var samurai = new Warrior('Samurai');

ninja.block = Position.high;
samurai.attack(ninja, Position.low);
// ninja.health should == 95
```
```python
ninja = Warrior('Hanzo Hattori')
samurai = Warrior('Ryōma Sakamoto')

samurai.block = 'l'
ninja.attack(samurai, 'h')
# samurai.health should be 90 now
```
```ruby
ninja = Warrior('Hanzo Hattori')
samurai = Warrior('Ryoma Sakamoto')

samurai.block = 'l'
ninja.attack(samurai, 'h')
# samurai.health should be 90 now
```
The warrios must be able to fight to the bitter end, and good luck to the most skilled!

Notice that health can't be below 0: once hit to 0 health, a warrior attribute `deceased` becomes `true`; if hit again, the `zombie` attribute becomes `true` too!
