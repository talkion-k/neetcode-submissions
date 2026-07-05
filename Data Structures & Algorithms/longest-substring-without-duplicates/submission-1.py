class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        freq = Counter()
        for r, char in enumerate(s):
            freq[char] += 1
            while freq[char] > 1:
                 freq[s[l]] -= 1
                 l += 1
            max_len = max(max_len, r - l + 1)
        return max_len
