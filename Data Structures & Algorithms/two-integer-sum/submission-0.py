class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        penis = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in penis:
                return [penis[diff], index]
            penis[num] = index
        
