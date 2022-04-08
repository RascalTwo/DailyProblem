[_metadata_:generated]: - "true"

# Learning TypeScript. Basic Types

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`5914c6ee51f1d39b5600001c`](https://www.codewars.com/kata/5914c6ee51f1d39b5600001c) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924094/typescript_s5czgr.svg" alt="TypeScript" title="TypeScript" width="50" />](solve.ts) |

<!-- INFO TABLE END -->

# Learning TypeScript. Basic Types

## Overview

In this kata you'll get familiar with TypeScript's basic types.<br>
If you have problems solving this kata please refer to this article: https://www.typescriptlang.org/docs/handbook/basic-types.html

## Task

### Boolean
- Export <code>var1Boolean</code> variable of boolean type with value <code>true</code>.

### Number
- Export <code>var2Decimal</code> variable of numeric type with decimal value <code>13</code>.
- Export <code>var3Hex</code> variable of numeric type with hex value <code>f00d</code>.
- Export <code>var4Binary</code> variable of numeric type with binary value <code>111111</code>.
- Export <code>var5Octal</code> variable of numeric type with octal value <code>744</code>.

### String
- Export <code>var6String</code> variable of string type with value <code>Hello, world!</code>.

### Array
- Export <code>var7Array</code> variable of array type with value <code>[1, 'test', {a: 3}, 4, 5]</code>.
- Export <code>var8NumericArray</code> variable of numeric generic array type with value <code>[1, 2, 3, 4, 5]</code>.

### Tuple
Tuple types allow you to express an array where the type of a fixed number of elements is known, but need not be the same. 
- Export <code>var9Tuple</code> variable of tuple type with value <code>['key', 12345]</code> - i.e. it should represent a value as a pair of a string and a number.

### Enums
- Export <code>var10Enum</code> variable with value <code>Color.Blue</code> from enum <code>export enum Color {Red = 1, Green = 2, Blue = 4}</code>.

### Any
We may need to describe the type of variables that we do not know when we are writing an application. These values may come from dynamic content, e.g. from the user or a 3rd party library. In these cases, we want to opt-out of type-checking and let the values pass through compile-time checks. To do so, we label these with the <code>any</code> type. 
- Export <code>var11ArrayOfAny</code> variable of <code>Array&lt;any&gt;</code> type with value <code>[1, 'test', {a: 3}, 4, 5]</code>.

### Void

- Export <code>var12VoidFunction</code> function that returns <code>void</code>.

### Null and Undefined

- Export <code>var13Null</code> variable with type and value <code>null</code>.
- Export <code>var14Undefined</code> variable with type and value <code>undefined</code>.

### Never
- Export <code>var15NeverFunction</code> function that returns <code>never</code> value.

**P.S.** Solved this kata? Take a look at other katas in "<a href="https://www.codewars.com/collections/learning-typescript">Learning TypeScript</a>" collection.
