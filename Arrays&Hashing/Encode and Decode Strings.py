"""
Problem: LeetCode 271 - Encode and Decode Strings

Key Idea:
We will create a string such that the individual words will follow their length and between them would be a delimiter ('#'). 
The delimiter would be used to find the length of the individual words in the list using which the strings would be separated from the encoded string.
"""

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            delimiter_pos = s.find("#", i)
            size = int(s[i:delimiter_pos])
            start_pos = delimiter_pos + 1
            end_pos = start_pos + size
            decoded.append(s[start_pos:end_pos])
            i = end_pos
        return decoded

# x = Solution()
# y = x.encode(["Hello","World"])
# z = x.decode(y)
# print(z)
