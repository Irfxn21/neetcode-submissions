class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h = {}

        for i in range (len(nums)):
            h[nums[i]] = i
        
        for i in range (len(nums)):
            diff = target - nums[i]
            if diff in h and i != h[diff]:
                return [i, h[diff]]
        