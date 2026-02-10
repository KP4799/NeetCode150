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
