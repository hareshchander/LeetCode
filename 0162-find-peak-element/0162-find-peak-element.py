class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
# Binary Search technique is used in it to get O(log N) time complexity and searching for an element in an array.
        left, right = 0, len(nums)-1

        while left < right:
            mid = (left+right)//2

            if nums[mid] < nums[mid+1]:
                left = mid + 1

            else:
                right = mid

        return left












