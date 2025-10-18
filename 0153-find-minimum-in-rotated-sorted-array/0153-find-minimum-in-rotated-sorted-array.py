class Solution:
    def findMin(self, nums: List[int]) -> int:

# We use this binary search approach because the array is sorted but rotated at some pivot.
        # range = 1 to 5
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            if  nums[mid] < nums[end]:
                end = mid
# Minimum could be at mid itself, so we must keep it in the search space

            else:
                start = mid +1

        return nums[start]











