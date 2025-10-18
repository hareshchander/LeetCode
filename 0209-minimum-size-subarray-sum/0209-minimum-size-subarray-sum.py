class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        summ = 0
        subarray_len_min = float('inf')

        for r in range(len(nums)):
            summ += nums[r]

            while summ >= target:
                subarray_len_min = min(subarray_len_min, r - l + 1)
                summ -= nums[l]
                l += 1 

        if subarray_len_min < float('inf'):
            return subarray_len_min
        else: 
            return 0




