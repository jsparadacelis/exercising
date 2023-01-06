from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = {}
        for anagram in strs:

            sorted_anagram = ''.join(sorted(anagram))
            if sorted_anagram in result:
                result[sorted_anagram].append(anagram)
            else:
                result[sorted_anagram] = [anagram]
        
        return [value for _, value in result.items()]
