from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        counter = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in counter:
                counter[sorted_word].append(word)
            else:
                counter[sorted_word] = [word]
        
        result = [value for value in counter.values()]
        return result
