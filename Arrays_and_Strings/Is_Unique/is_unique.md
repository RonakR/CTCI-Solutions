# Is Unique

Implement an algorithm to determine if a string hsa all unique characters. What if you can not user additional data
structures?

## Steps to Solve Problem
#### Listen
- String is not necessarily in alphabetical order
- no size limit
- try data structure first, then optimize to not use data structure.
- Maybe check for palindrome?

#### Example
- `input: "TestString" output: false`
- `input: "abcdefgh" output: true`

#### Brute Force
- Run through each character and compate to rest of the string O(N<sup>2<sup>)
- Run through each character and store in hash table, if there is a collision it is not unique. Time: O(N) Space: O(N)

#### Optimize
- Look for BUD
- DIY
- Simplify & Generalize
- Base Case and Build
- Data Structure Brainstorm

#### Implement
#### Walk Through
#### Test
