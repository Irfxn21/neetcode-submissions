class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h = {}

        for i in range(len(nums)):
            h[nums[i]] = i


        for j in range(len(nums)):
            diff = target - nums[j]
            if diff in h and h[diff] != j:
                return [j,h[diff]]

        