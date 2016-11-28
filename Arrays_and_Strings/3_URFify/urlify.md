# URLify

Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the
end to hold hte additional characters, and that you are given the "true" length of the string.
## Steps to Solve Problem
#### Listen
- "string as sufficent space at the end to hold additional characters": Make the change in place
- "given the true length of the string": Is there a way to reverse engineer the string given true length, and string length

#### Example
- `input: "Mr John Smith    ", 13 output: "Mr%20John%20Smith"
- `input: "Test   Test      ", 11 output: "Test%20%20%20Test"

#### Brute Force
- In Python strip > split(" "), '%20'.join lists. (Not in place)
#### Optimize
- Look for BUD
    - Split list as is, run from back and move items to the back of list. On space insert '%20'. Big O(N)

#### Implement
#### Walk Through
#### Test
