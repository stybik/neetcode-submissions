class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = set(nums)
        return False if len(ans) == len(nums) else True