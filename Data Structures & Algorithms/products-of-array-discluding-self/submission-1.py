class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        left[0] = nums[0]
        right[0] = nums[-1]
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i]
            right[i] = right[i - 1] * nums[-(i + 1)]
        ans = [0] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                ans[i] = right[-2]
            elif i == len(nums) - 1:
                ans[i] = left[-2]
            else:
                l = left[i - 1]
                r = right[-(i + 2)]
                ans[i] = l * r
        return ans
