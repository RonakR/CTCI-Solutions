# Delete Middle Node

Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the
exact middle) of a singly linked list, given only access to that node.

## Steps to Solve Problem
#### Listen
- What to do when given the first or last node?
- singly linked list
- Only given access to the one node. 
- Watch out for nulls

#### Example
- `input: c from list a->b->c->d->e->f, output: a->b->d->e->f`

#### Brute Force
- Replace contents of current node with contents of the next node.
 - Which means, the current node retains it's original reference but it's data and next are that of the next item in the list.
 
#### Optimize
- Look for BUD
- DIY
- Simplify & Generalize
- Base Case and Build
- Data Structure Brainstorm

#### Implement
#### Walk Through
#### Test
