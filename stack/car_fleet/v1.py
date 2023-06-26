from typing import List


class Solution:

    def will_collide(self):
        pass

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # sorting cars by their position
        cars_data = zip(position, speed)
        sorted_data = list(sorted(cars_data, key=lambda car: car[0]))

        # [(0,1), (3,3), (5,1), (8,4), (10,2)]
        stack = []
        for pos, speed in sorted_data[::-1]:

            time_to_target = (target - pos)/speed
            if not stack or (stack and time_to_target > stack[0]) :
                stack.insert(0, time_to_target)
        return len(stack)

"""
[(0,1), (3,3), (5,1), (8,4), x(10,2)]
stack = [1]
[(0,1), (3,3), (5,1), x(8,4), (10,2)]
stack = [1]
[(0,1), (3,3), x(5,1), (8,4), (10,2)]
stack = [7,1]
[(0,1), x(3,3), (5,1), (8,4), (10,2)]
stack = [7,1]
[x(0,1), (3,3), (5,1), (8,4), (10,2)]
stack = [11,7,1]
"""

if __name__ == '__main__':

    sol = Solution()
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    print(sol.carFleet(target=target, position=position, speed=speed))
