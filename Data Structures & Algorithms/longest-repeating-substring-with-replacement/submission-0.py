class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # xxyyyxx k = 2 -> replace xx, k = 3 -> replace yyy
        l = 0
        maxFreq = 0
        freq = Counter()
        for r, char in enumerate(s):
            freq[char] += 1
            maxFreq = max(maxFreq, freq[char])
            if r - l + 1 - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
        return len(s) - l
            
        