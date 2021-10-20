# Poker Hands

<!-- INFO TABLE BEGIN -->

| Provider                                            | Source                                                 | Solutions                                                                                                                                    |
| :-------------------------------------------------: | :----------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------: |
| [CodingDojo](../../../docs/providers/CodingDojo.md) | [`PokerHands`](https://codingdojo.org/kata/PokerHands) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/java_un8ru7.svg" alt="Java" title="Java" width="50" />](solve.java) |

<!-- INFO TABLE END -->

Parse cards that belong to named users, compare the two poker hands and return which - and with what - if either, wins.

## Examples

| Input                                         | Output                                    |
| --------------------------------------------- | ----------------------------------------- |
| `Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C AH` | `White wins. - with high card: Ace`       |
| `Black: 2H 4S 4C 2D 4H White: 2S 8S AS QS 3S` | `Black wins. - with full house: 4 over 2` |
| `Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C KH` | `Black wins. - with high card: 9`         |
| `Black: 2H 3D 5S 9C KD White: 2D 3H 5C 9S KH` | `Tie.`                                    |
