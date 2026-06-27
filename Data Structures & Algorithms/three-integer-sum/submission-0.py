class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = []
        nums.sort()
        for low in range(len(nums)):
            mid, high = low + 1, len(nums) - 1
            if low > 0 and nums[low] == nums[low - 1]:
                continue
            while mid < high:
                test = nums[low] + nums[mid] + nums[high]
                if test == 0:
                    sums.append([nums[low], nums[mid], nums[high]])
                    mid += 1
                    high -= 1
                    while mid < len(nums) - 1 and nums[mid] == nums[mid - 1]:
                        mid += 1
                    while high > mid and nums[high] == nums[high + 1]:
                        high -= 1
                elif test < 0:
                    mid += 1
                else:
                    high -= 1
        return sums

                    
        