"""
Problem: LeetCode 238 - Product of Array Except Self

Key Idea:
We iterate through the list using nested for loops, multiplying the numbers except the current number.

Time Complexity:
The time complexity of this approach is O(n2), where n is the number of elements in the input list.
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product = 1
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                product *= nums[j]
            result.append(product)
            product = 1

        return result
    
# x = Solution()
# y = x.productExceptSelf([1,2,3,4])
# print(y)
