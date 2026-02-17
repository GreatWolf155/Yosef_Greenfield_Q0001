"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without
duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

s = str(input("Please input a string of characters: "))
max_len = 0
while True:
    current_len = 0
    tester = []
    for i in range(len(s)):
        if s[i] not in tester:
            tester.append(s[i])
            current_len += 1
        else:
            s = s[1:]
            break
        if current_len > max_len:
            max_len = current_len
    if max_len >= len(s):
        break
print(max_len)