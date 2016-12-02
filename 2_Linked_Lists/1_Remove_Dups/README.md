# Remove Dups

Write code to remove duplicates from an unsorted linked list. FOLLOW UP: How would you solve this problem if a
temporary buffer is not allowed?

## Steps to Solve Problem
#### Listen
- list is unsorted
- follow up tells us that a temporary buffer might be helpful for the first part
- Singly or doubly linked list? Assuming singly
- Data type? ints, strings, etc. Assming anything
- for string, does case matter?

#### Example
- `input: 4->1->2->4->4->5->3->6->3, output: 4->1->2->5->3->6`
- `input: aligator->aardvark->zebra->aardvark, output: aligator->aardvark->zebra`

#### Brute Force
- For each item in list compare to rest of the items. Standard O(N<sup>2</sup>) soln.

#### Optimize
- Look for BUD
 - Utilize hash table/dict. Run through list, if item's in dict remove the currect item from list, else add current item to dict. Time: O(N), Space: O(N)
 - FOLLOW UP optimization: For each character use a runner to look through the rest of the list checking for dupicates. O(N<sup>2</sup>)

#### Implement
#### Walk Through
#### Test
