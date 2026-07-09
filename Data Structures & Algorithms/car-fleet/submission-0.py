class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        info = [(p, s) for p, s in zip(position, speed)]
        info.sort(key = lambda tup: tup[0], reverse = True)
        # time to target is (target - p) / s
        st = []
        for p, s in info:
            st.append((target - p) / s)
            if len(st) > 1 and st[-1] <= st[-2]:
                st.pop()
        return len(st)