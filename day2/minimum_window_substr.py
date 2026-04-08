"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "BANCADOBECODE", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""

# Brute force
s = "ADOBECODEBANC"
t = "ABC"
start_i = -1
from collections import Counter
def min_window(s, t):
    l , r = 0, 0
    t_count = Counter(t)
    min_len = float('inf')
    min_str = ""
    have = 0
    while r < len(s):
        sub_str = s[l:r+1]
        for i in sub_str:
            if i in t_count and t_count[i] >0:
                have += 1
                t_count[i] -= 1
            else:
                t_count[i] = t_count.get(i, 0) - 1
        while have == len(t) and min_len > len(sub_str):
            #valid string
            min_len = len(sub_str)
            min_str = s[l:r+1]
            l += 1
        else:
            r += 1


    
print(min_window(s, t))



        

