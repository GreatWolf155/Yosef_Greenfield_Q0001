"""
6. Zigzag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a
given number of rows like this: (you may want to display this pattern
in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion
given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Explanation:
P   A   H   N
A P L S I I G
Y   I   R

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

s = "PAYPALISHIRING"
numRows = 5
# will crash due to index range if numRows = 1
# and skip if there is no need to do the math
if numRows == 1 or numRows >= len(s):
    print(s)
else:
    # Let's make rows of characters to be read off
    rows = [""] * numRows

    # need to know where we are at any given step
    current_row = 0

    #add characters to the bucket
    for char in s:
        rows[current_row] += char

        # direction to move next
        if current_row == 0:
            step = 1
        if current_row == (numRows - 1):
            step = -1
        current_row += step
    for item in rows:
        print(item, end='')


