# Check Permutation

Given two string, write a method to decide if one is a permutation of the other

- check_permuation_1 is my first answer, run through first string and remove correspoding character in second string. O(N<sup>2</sup>)
- check_permutation_2 populate hash table with number of character occurrences in first string, compare occurrences in second string. O(N)

## Steps to Solve Problem
#### Listen
- not necessarily sorted
- can't be of different lengths
- Forgot:
  - Case sensitive
  - whitespace
#### Example
- `input: "sales", "lases" output: True`
- `input: "trees", "treed" output: False`

#### Brute Force
- run through first string and check if character is in second string. If it is, remove it from second sting. O(n<sup>2</sup>)

#### Optimize
- sort the two strings and compare them. O(N logN + N logN) = O(N logN)
- populate hash table with contents of first string, O(f), loop through second string, O(s) and check for collisions. O(N + N) =
  - Consider collisions in the first string, i.e. "TestString" has two 't's and 's's

#### Implement
#### Walk Through
#### Test
