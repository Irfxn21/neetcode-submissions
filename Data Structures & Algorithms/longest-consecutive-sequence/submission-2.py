class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()

        count = 0
        longest = 0

        if not nums:
            return 0

        for i in range(len(nums)-1):

            if nums[i] == nums[i+1]:
                continue

            if (nums[i+1] - nums[i]) == 1:
                count += 1
            else:
                count += 1
                longest = max(longest, count)
                count = 0

        longest = max(longest, count+1)
        return longest


        