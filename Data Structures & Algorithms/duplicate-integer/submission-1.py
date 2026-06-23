class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        converted_set = set(nums)
        if len(converted_set) != len(nums):
            return True
        else:
            return False