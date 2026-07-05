class Solution:
    def countSubstrings(self, s: str) -> int:
        l, r = 0, 0
        ans = 0
        def palHelper(l, r):
            nonlocal ans
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if s[l:(r + 1)]:
                    ans += 1
                l -= 1
                r += 1
        for i in range(len(s)):
            palHelper(i, i)
            palHelper(i, i + 1)
        return ans