# We use the binary search as the time complexity requirement is O(logn) and secondly we want to search an element.
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:

        # Brute Force approcah

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i

        # return -1

# Binary Search Technique

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:

                if nums[l] <= target < nums[mid]:
                    r = mid -1

                else:
                    l = mid + 1

            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1

                else:
                    r = mid -1

        return -1

