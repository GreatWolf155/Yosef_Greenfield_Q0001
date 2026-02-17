"""
2. Add Two Numbers
Medium
Topics
premium lock icon
Companies
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
num1 = 0
num2 = 0
for i in range(len(l1)):
    num1 += l1[i] * (10 ** i)
for i in range(len(l2)):
    num2 += l2[i] * (10 ** i)
result = num1 + num2
result = str(result)
result = list(result)
result.reverse()
for index in range(len(result)):
    result[index] = int(result[index])
print(result)
