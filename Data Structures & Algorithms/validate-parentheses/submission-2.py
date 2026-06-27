class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for c in s:
            if c in '({[':
                check.append(c)
            elif check and check[-1] == pairs[c]:
                check.pop()
            else:
                return False
        return not check