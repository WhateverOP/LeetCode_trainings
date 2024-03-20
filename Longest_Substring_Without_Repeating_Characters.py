'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0
    max_substr_len = 1
    now_substr_len = 1
    i = 0
    j = 1
    letter_index_dict = {s[i]:i}
    while j < len(s):
        print(f'i = {i}, j = {j}, now = {now_substr_len}, max = {max_substr_len}')
        if s[j] not in letter_index_dict:
            letter_index_dict[s[j]] = j
            j += 1
            now_substr_len += 1
            if now_substr_len > max_substr_len:
                max_substr_len = now_substr_len
        else:
            i = letter_index_dict[s[j]] + 1
            letter_index_dict[s[j]] = j
            j += 1
            if now_substr_len > max_substr_len:
                max_substr_len = now_substr_len
            now_substr_len = j - i
    return max_substr_len





def lengthOfLongestSubstring(s):
    ls = ""
    l,r = 0,0
    ci = {}

    while r < len(s):
        c = s[r]
        if c not in ci:
            ci[c] = r  
        else:
            if ci[c] + 1 > l:
                l = ci[c] + 1
            ci[c] = r
            
        if len(ls) < r-l+1:
            ls = s[l:r+1]

        r += 1
        
    if len(ls) < r-l:
        ls = s[l:r]   
        
    return len(ls)
        

s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# s = "a"
# s = "au"
# s = "abba"
# s = "tmmzuxt"
ans = lengthOfLongestSubstring(s)
print(ans)