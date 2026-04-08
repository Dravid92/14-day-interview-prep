"""
Given a string s, find the length of the longest substring without duplicate characters.

 

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
 
"""
# def find_lswor(s):
#     max_count = 0
#     max_word = ''
#     for i in range(len(s)-2):
#         j = i +1 
#         l_str = ""
#         while j<len(s) and s[j] not in l_str:
#             l_str += s[j]
#             j += 1
#         max_count = max(max_count, len(l_str))  
#         max_word = s[i:j+1]  
#     return max_count, max_word



def find_lswor(s):
    l = 0
    max_count = 0
    sub_Str = set()
    for r in range(len(s)):
        while s[r] in sub_Str:
            sub_Str.remove(s[l])
            l += 1
        sub_Str.add(s[r])
        max_count = max(max_count,len(sub_Str))
    return max_count

s = "abcabcbb"
print(find_lswor(s))