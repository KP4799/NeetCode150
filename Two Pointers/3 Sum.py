"""
Problem: LeetCode 15 - 3Sum

Key Idea:
To find all unique triplets that sum to zero, we can use a two-pointer approach. First, we sort the input array 'nums' in an ascending order. 
Then, we iterate through the array with a fixed first element (i). For each fixed first element, we use two pointers (left and right) to find the other two elements that sum to the negation of the fixed first element. 
As the array is sorted, we can move these two pointers towards each other to efficiently find all possible triplets.

Time Complexity:
The time complexity of this solution is O(n^2), where n is the number of elements in the input array 'nums'. Sorting the array takes O(nlogn) time, and the two-pointer approach iterates through the array once, performing a linear search for each element.

Space Complexity:
The space complexity is O(1) since we are not using any additional data structures that depend on the input size. We only use a constant amount of extra space for the three pointers and other variables.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        indices = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            j = i + 1
            k = len(nums) - 1
            
            while j<k:
                current = nums[j] + nums[k]
                
                if current == -nums[i]:
                    indices.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                
                elif current < -nums[i]:
                    j += 1
                else:
                    k -= 1
                    
        return indices

# x = Solution()
# y = x.threeSum([-1,0,1,2,-1,-4])
# print(y)
