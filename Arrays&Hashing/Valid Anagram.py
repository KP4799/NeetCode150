class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # set_s = (i for i in s)
        # set_t = (i for i in t)

        # if sorted(set_s) == sorted(set_t):
        #     return True
        # else:
        #     return False

        if len(s) != len(t):
            return False

        for i in set(s):
            if s.count(i) != t.count(i):
                return False

        return True