# https://www.youtube.com/watch?v=Nxx73SXKLto

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ans = max(nums)   # OR, you can select this ans = 0
        Max, Min = 1, 1    # Lets suppose bcz by supposing 0 ans will get zero.

        for n in nums:
            temp = Max * n
            Max = max(Max*n, Min*n, n)
            Min = min(temp, Min*n, n)   
            #Here temp is used bcz we need previous value of Max
            
            ans = max(ans, Max)

        return ans


























        