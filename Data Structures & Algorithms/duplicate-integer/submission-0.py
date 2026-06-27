class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        inArray = set()
        for num in nums:
            if num in inArray:
                return True
            inArray.add(num)
        return False