class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area: min(heights[l], heights[r]) * (r - l)
        area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            area = max(area, min(heights[l], heights[r]) * (r - l))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return area