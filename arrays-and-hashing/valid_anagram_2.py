from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for s_it, t_it in zip(sorted(s), sorted(t)):
            if s_it != t_it:
                return False
        return True
