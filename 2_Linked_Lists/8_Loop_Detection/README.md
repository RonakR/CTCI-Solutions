# Loop Detection

Given a circular linked list, implement an algorithm that returns the nodes at the beginning of the loop.
#### Definition:
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list 

## Steps to Solve Problem
#### Listen
- singly or doubly linked list? Assuming singly
- Similar to 2.7, but instead of looking for intersection between two lists, you're looking for it in one list. 

#### Example
- `input: A->B->C->D->E->C (same C as earlier), output: C`
- `input: A->B->C->D->E->F, output: False`

#### Brute Force
- Run through list, add each node to hashmap with the value of node.next. Time: O(N), Space: O(N)
 - If a node.data is in the hashmap, check if the node.next is similar
 - If a node.data is in the hashmap but node.next is not similar, add the node as entry to hashmap.
 - If node.data doesn't match anything in the hashmap, keep moving
 
#### Optimize
- Look for BUD
- DIY
- Simplify & Generalize
- Base Case and Build
- Data Structure Brainstorm

#### Implement
#### Walk Through
#### Test
