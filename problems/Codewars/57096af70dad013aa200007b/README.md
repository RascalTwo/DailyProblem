[_metadata_:generated]: - "true"

# Logical calculator

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`57096af70dad013aa200007b`](https://www.codewars.com/kata/57096af70dad013aa200007b) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

## Your Task

Given an array of Boolean values and a logical operator, return a Boolean result based on sequentially applying the operator to the values in the array.

## Examples

1) booleans = `[True, True, False]`, operator = `"AND"`
 * `True` `AND` `True`  -> `True`
 * `True` `AND` `False` -> `False`
 * return `False`

2) booleans = `[True, True, False]`, operator = `"OR"`
 * `True` `OR` `True`  -> `True`
 * `True` `OR` `False` -> `True`
 * return `True`

3) booleans = `[True, True, False]`, operator = `"XOR"`
 * `True` `XOR` `True`  -> `False`
 * `False` `XOR` `False` -> `False`
 * return `False`

## Input
1) an array of Boolean values `(1 <= array_length <= 50)`
2) a string specifying a logical operator: `"AND"`, `"OR"`, `"XOR"`

## Output
A Boolean value (`True` or `False`).
