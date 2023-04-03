from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create a hash map to now how mant times an elem is in the arr
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        # let's use the bucket sort algo. Create a list of lists
        freq = [[] for i in range(len(nums) + 1)]
        for value, count in counter.items():
            # each index in the bucket will represent the appereances for each value in nums
            freq[count].append(value)

        result = []
        # iterate over the frequence bucket 
        for i in range(len(freq)-1,0,-1):
            # iterate over each internal list
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result

if __name__ == '__main__':

    sol = Solution()
    nums = [1]
    k = 1
    sol.topKFrequent(nums, k)
