from typing import List

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        frequencies = {}
        for num in nums:
            
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[num] += 1
        
        sorted_freq = defaultdict(list)
        for num, freq in frequencies.items():
            sorted_freq[freq].append(num)
        
        result = []
        for i in range(len(nums), -1, -1):
            if i in sorted_freq and len(result) < k:
                if k == len(sorted_freq[i]):
                    return sorted_freq[i]
                result.extend(sorted_freq[i])
        return result
        
if __name__ == "__main__":

    sol = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    sol.topKFrequent(nums=nums, k=k)
