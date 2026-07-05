class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longestHelper(s, isEven):
            l, r = 0, int(isEven)
            longest = 0
            longestIndex = 0
            for i, char in enumerate(s):
                while r < len(s) and s[l] == s[r] and l >= 0:
                    if (r - l + 1) > longest:
                        longestIndex = l
                        longest = r - l + 1
                    l -= 1
                    r += 1
                l = i
                r = i + isEven
            return s[longestIndex:(longestIndex + longest)]
        odd = longestHelper(s, False)
        even = longestHelper(s, True)
        if len(odd) > len(even):
            return odd
        else:
            return even
        