# Is Unique

Implement an algorithm to determine if a string hsa all unique characters. What if you can not user additional data
structures?

- is_unique_1 is my answer with a data structure
- is_unique_2 is my final answer (w/out data structure)
- is_unique_book is the answer from the book


## Steps to Solve Problem
#### Listen
- String is not necessarily in alphabetical order
- at most the string can't be greater than 128 characters
- try data structure first, then optimize to not use data structure.
- Maybe check for palindrome?
- Forgot to ask
  - ASCII or Unicode

#### Example
- `input: "TestString" output: false`
- `input: "abcdefgh" output: true`

#### Brute Force
- Run through each character and compate to rest of the string O(N<sup>2</sup>)
- Run through each character and store in hash table, if there is a collision it is not unique. Time: O(N) Space: O(N)

#### Optimize
- Look for BUD
  - Remove hash table
  - Sort string, O(N logN), walk through the string and compare adjacent values O(N) = O(N<sup>2</sup> logN)

#### Implement
- Sort string
- Consider capital letters
- Walk through sorted string

#### Walk Through
#### Test

