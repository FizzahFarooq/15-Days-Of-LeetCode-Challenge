class Solution:
    def lengthOfLongestSubstring(self, s):
        last_index = {}
        start = 0
        max_len = 0

        for i in range(len(s)):
            ch = s[i]
            if ch in last_index and last_index[ch] >= start:
                start = last_index[ch] + 1
            last_index[ch] = i
            cur_len = i - start + 1
            if cur_len > max_len:
                max_len = cur_len

        return max_len
