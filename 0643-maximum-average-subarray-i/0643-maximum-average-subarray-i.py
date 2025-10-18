class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        i = k
        while i < len(nums):
            window_sum = window_sum - nums[i-k] + nums[i]

            if window_sum > max_sum:
                max_sum = window_sum

            i += 1

        average = max_sum/k

        return average

