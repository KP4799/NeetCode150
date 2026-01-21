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