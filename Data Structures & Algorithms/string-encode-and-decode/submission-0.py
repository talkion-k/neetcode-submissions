class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += f"{len(s):03}" + s
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            length = int(s[i:i + 3])
            i += 3
            ans.append(s[i:i + length])
            i += length
        return ans
