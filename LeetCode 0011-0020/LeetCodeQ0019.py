"""
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.


Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]


Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?
"""

"""
swap list to list of lists, where the first value is the list value, and the second is the list index of the next item
the last index value will be None
add the value to a new list
if the second value is None, stop
if the second value is greater than the current index, add an extra one to the current index
"""

head = [1,2,3,4,5]
n = 2

linked = []
new_linked = []
# Come back to this
# next = i+1

for i in range(len(head)):
    if i != len(head) - 1:
        linked.append([head[i], i + 1])
    else:
        linked.append([head[i], None])
for i in range(len(linked)):
    if i == len(linked) - n:
        linked[i][1] = 'skip'
        linked[i-1][1] += 1
index = 0
while True:
    new_linked.append(linked[index][0])
    if linked[index][1] is None:
        break
    if linked[index][1] > index + 1:
        index += 2
    else:
        index += 1
print(new_linked)
