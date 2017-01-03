# Validate BST

Implement a function to check if a binary tree is a binary search tree

## Steps to Solve Problem
#### Listen
- Tree given to us is Birary tree
- BST would mean all left decendants <= n < all right decendants
 - Duplicates will be on left or right
- Soln here doesn't care about perfect/complete/full.

#### Example
- `input: 8:[7:[6:[None None],7:[None None]],10:[9:[None None],15:[None None]]], output: True`
- `input: 8:[7:[6:[None None],9:[None None]],10:[None 15:[None None]]], output: False`

#### Brute Force
- In order traversal from root. Variable to store max so far
 - on "visit" check if current value is greater than or equal to max so far. 
 - if that is ever false then it's not a BST.

#### Optimize
- Look for BUD
- DIY
- Simplify & Generalize
- Base Case and Build
- Data Structure Brainstorm

#### Implement
#### Walk Through
#### Test
