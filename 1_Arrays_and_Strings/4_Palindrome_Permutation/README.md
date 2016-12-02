# Palindrome Permutation

Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that
is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be
limited to just dictionary words.

## Steps to Solve Problem
#### Listen
- Palindrome does not need to be in the dictionary
- Check through all permutations and check for palindrome O(N!)
- The examples in the book show that case doesn't matter
- Forgot:
    - to deal with spaces
    - to lower the case
#### Example
- `input: "Tact Coa" output: True`
- `input: "test" output: False`
#### Brute Force
- Check for letter pairs, if there is more than one character with out a pair it's not a palindrome.
#### Optimize
- Look for BUD
- DIY
- Simplify & Generalize
- Base Case and Build
- Data Structure Brainstorm

#### Implement
#### Walk Through
#### Test
