from typing import List

class Solution:
    

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []
        """
        border cases:
            1. intervals: [[3, 4], [5, 6]]; newInterval: [1, 2] -> non-overlap. Due to 1 < 3 and we know intervals
            is sorted just add newInterval to res and the the rest of intervals.
            2. intervals: [[3, 4], [9, 16]]; newInterval: [7, 8] -> non-overlap. In this case the first time in newInterval
            is greather than the last one. It means in the future we could want to add this new interval.
            3. We overlap with the current interval. So, just update newInterval and let the for-loop add the newInterval
            to existing list
        """
        for i in range(len(intervals)):

            # if newInterval is before interval
            interval = intervals[i]
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                result += intervals[i:]
                # we don't need to iterate bc we found the slot of newInterval
                return result
            elif newInterval[0] > interval[1]:
                result.append(interval)
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        result.append(newInterval)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
