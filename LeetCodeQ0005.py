"""
5. Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""

s = str(input("Please input string: "))
lps = 0
answer = None
if len(s) >= 1:
    lps += 1
while len(s) > lps:
    temp = s[::-1]
    while len(temp) > lps:
        if temp in s:
            lps = len(temp)
            answer = temp
        temp = temp[1:]
    s = s[1:]
print(answer)
print(lps)
