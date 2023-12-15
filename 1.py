# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

from typing import List

# 最初の回答
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(nums) != len(set(nums))

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    

# 関数の実行
nums = [1,2,3,1]
solution = Solution()
print(solution.containsDuplicate(nums))

nums = [1,2,3,4]
print(solution.containsDuplicate(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(solution.containsDuplicate(nums))
