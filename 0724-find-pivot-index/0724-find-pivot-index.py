class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            
            if right_sum == left_sum:
                return i
            
            # Update the left sum by adding the current element
            left_sum += nums[i]
        
        # Step 4: If no pivot index is found, return -1
        return -1

# Example usage:
# Create an instance of the Solution class
solution = Solution()

# Define the input array
nums = [1, 7, 3, 6, 5, 6]

# Call the pivotIndex method and print the result
print(solution.pivotIndex(nums))  # Output: 3