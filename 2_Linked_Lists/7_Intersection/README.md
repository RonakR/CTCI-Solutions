# Intersection

Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, no value. That is, if the kth node of the first list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.

## Steps to Solve Problem
#### Listen
- singly linked list
- how much of an intersection? All values after the first similar one need to the the same between the two lists
 - last node should be the same 
- `by reference not value` i.e. 1->3->7->4, 2->3->4->5 not intersecting, 1->3->7->4, 2->3->7->4 intersecting on 3. 

#### Example
- `input: 1->3->7->4, 2->3->4->5 output: False`
- `input: 1->3->7->4, 2->3->7->4 output: 3`

#### Brute Force
- thinking runner on both lists comparing each node. O(A+B)
 - if no nodes are the same, not intersecting
 - if there are a couple similar nodes but they don't follow the same items later, not intersecting
 - if there is a similar node and the rest of the nodes are similar too, return the first node of the interesction
 
#### Optimize
- Look for BUD
- DIY
- Simplify & Generalize
- Base Case and Build
- Data Structure Brainstorm

#### Implement
#### Walk Through
#### Test
