# Route Between Nodes

Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

## Steps to Solve Problem
#### Listen
- Directed graph
- Isn't specifically acyclic, so can be cyclic. 
- "Between two nodes" does that mean a->b and b<-a or just one of those. 
 - Going with one those. 
- Storing these in an adjancency list

#### Example
- input params: Graph, nodeOne, nodeTwo
- `input: {a:[b,f], b:[d], c:[b], d:[a], e:[a], f:[e]}, a, c output: True`

#### Brute Force
- BFS from nodeOne to nodeTwo, unmark all marked nodes, BFS from nodeTwo to nodeOne

#### Optimize
- Look for BUD
- DIY
- Simplify & Generalize
- Base Case and Build
- Data Structure Brainstorm

#### Implement
#### Walk Through
#### Test
