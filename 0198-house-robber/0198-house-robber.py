class Solution:
    def rob(self, nums: List[int]) -> int:
        r1 = 0     # These are the values not index
        r2 = 0
        for n in nums:
            temp = max(r1+n, r2)
            r1 = r2
            r2 = temp

        return r2

'''This will iterate through the values not the index for index iteration we use like: for n in range(len(nums))'''










        