class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = {}

        for c in s:
            letters[c] = letters.get(c, 0) + 1
        
        for c in t:
            letters[c] = letters.get(c, 0) - 1
        
        for i in letters.values():
            if i != 0:
                return False
        
        return True