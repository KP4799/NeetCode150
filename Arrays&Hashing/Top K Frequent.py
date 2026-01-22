"""
Problem: LeetCode 347 - Top K Frequent Elements

Key Idea:
To find the k most frequent elements in the given list, we can use a hash map (dictionary in Python) to keep track of each element.
We assign the elements to a list represented by the same element (key). Then we sort the hash map in reverse order based on the length of these lists.
The top K keys return the most frequent items.

Time Complexity:
The time complexity of this approach is O(n + k*log(n)), where n is the number of elements in the input list. Building the frequency map takes O(n) time, and inserting k elements into the min-heap takes O(k*log(n)) time.

Space Complexity:
The space complexity is O(n) because we need to store the frequency map of all elements in the input list. Additionally, the min-heap will also have a space complexity of O(n) in the worst case if all elements are unique.
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = []
            hashmap[i].append(i)
        
        result = sorted(hashmap.keys(), key=lambda x: len(hashmap[x]), reverse=True)
    
        return result[:k]

        
# x = Solution()
# y = x.topKFrequent([1,2,2,3,3,3],2)
# print(y)
