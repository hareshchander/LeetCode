class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        result = [1] * n
        
        prefix = 1
        for i in range(n):
            result[i] = prefix 
            prefix = prefix * nums[i]
        
        postfix = 1
        for i in reversed(range(n)):
            result[i] = result[i] * postfix 
            postfix = postfix * nums[i]  
        
        return result


        