class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        h = {}
        output = []
        sum = 1

        for i in range(len(nums)):
            h[i] = nums[i]
        
        #for i in range(len(nums)):
            #if i 
        
        for i in range(len(nums)):
            sum = 1
            for j in range(len(nums)):
                if i != j:
                    sum = sum * nums[j]

            output.append(sum)

        return output


