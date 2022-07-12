[_metadata_:generated]: - "true"

# Thinkful - Object Drills: Quarks

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5882b052bdeafec15e0000e6`](https://www.codewars.com/kata/5882b052bdeafec15e0000e6) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

## Background

You're modelling the interaction between a large number of quarks and have decided to create a `Quark` class so you can generate your own quark objects.

[Quarks](https://en.wikipedia.org/wiki/Quark) are fundamental particles and the only fundamental particle to experience all four fundamental forces.

## Your task

Your `Quark` class should allow you to create quarks of any valid color (`"red"`, `"blue"`, and `"green"`) and any valid flavor (`'up'`, `'down'`, `'strange'`, `'charm'`, `'top'`, and `'bottom'`).

Every quark has the same `baryon_number` (`BaryonNumber` in `C#`): 1/3.

```if:factor
In Factor, the `<quark>` constructor should be defined. This will be tested to ensure quark objects are initialized correctly.
```

Every quark should have an `.interact()` (`.Interact()` in `C#`) method that allows any quark to interact with another quark via the strong force. When two quarks interact they exchange colors.

## Example

```python
>>> q1 = Quark("red", "up")
>>> q1.color
"red"
>>> q1.flavor
"up"
>>> q2 = Quark("blue", "strange")
>>> q2.color
"blue"
>>> q2.baryon_number
0.3333333333333333
>>> q1.interact(q2)
>>> q1.color
"blue"
>>> q2.color
"red"
```
```csharp
>>> Quark q1 = new Quark("red", "up");
>>> q1.Color;
"red"
>>> Quark q2 = new Quark("blue", "strange");
>>> q2.Color;
"blue"
>>> q2.BaryonNumber;
0.3333333333333333
>>> q1.Interact(q2);
>>> q1.Color;
"blue"
>>> q2.Color;
"red"
```
```factor
[let
  "red" "up" <quark> :> q1
  q1 color>> .  ! "red"
  "blue" "strange" <quark> :> q2
  q2 color>> .  ! "blue"
  q2 baryon-number>> .  ! 1/3
  q1 q2 interact
  q1 color>> .  ! "blue"
  q2 color>> .  ! "red"
]
```
