"""
Problem: LeetCode 128 -Longest Consecutive Sequence

Key Idea:
To find the longest consecutive subsequence, we create a dictionary which holds the current number as the key and the maximum length of sequence possible from that number as the value. We then return the maximum value of all to give the largest consecutive sequence.

Time Complexity:
The time complexity of this solution is O(n), where n is the number of elements in the input array 'nums'. The dictionary operations (addition and lookup) take O(1) time on average, and we perform these operations for each element once.

Space Complexity:
The space complexity is O(n), where n is the number of elements in the input array 'nums'. In the worst case, the set will store all elements from the input array if they are all distinct.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        lengths = {}
        for i in nums:
            current = i

            y = i + 1 in nums
            while y:
                count += 1
                current += 1
                y = current + 1 in nums
        
            lengths[i] = count
            count = 1
        
        if not lengths:
            return 0
        z = max(lengths.values())
        return z

# x = Solution([0,3,2,5,4,6,1,1])
# y = x.longestConsecutive()
# print(y)
