class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = {}
        majority = answer = 0
        for num in nums:
            result[num] = 1 + result.get(num, 0)
            if result[num] > majority:
                answer = num
                majority = result[num]

        return answer