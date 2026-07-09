class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        info = [(p, s) for p, s in zip(position, speed)]
        info.sort(key = lambda tup: tup[0], reverse = True)
        # time to target is (target - p) / s
        prev = 0
        ans = 1
        for i, (p, s) in enumerate(info):
            if i == 0:
                # prev = current
                prev = (target - p) / s
            else:
                curr = (target - p) / s
                if prev < curr:
                    ans += 1
                    prev = curr
        return ans