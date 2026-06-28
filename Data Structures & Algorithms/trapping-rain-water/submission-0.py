class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        left = [height[0]] * l
        right = [height[l - 1]] * l
        area = 0
        for i in range(1, l):
            left[i] = max(height[i], left[i - 1])
            right[l - i - 1] = max(height[l - i - 1], right[l - i])
        for i in range(1, l):
            area += min(left[i], right[i]) - height[i]
        return area

