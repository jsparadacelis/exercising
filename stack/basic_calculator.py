from typing import List

TEST_CASES = [
    {
        "input": {
            "s": "1 + 1"
        },
        "result": 2
    },
    {
        "input": {
            "s": " 2-1 + 2 "
        },
        "result": 3
    },
    {
        "input": {
            "s": "(1+(4+5+2)-3)+(6+8)"
        },
        "result": 23
    }

]


class Solution:
    def calculate(self, s: str) -> int:
        

        curr_number = 0
        sign = 1
        result = 0
        stack = []
        for char in s:

            if char == " ":
                continue

            if char.isdigit():
                
                # if we have curr_number != it means curr_number used to be the first
                # digit of an entire number
                # 52: curr = 5 -> curr = curr*10 + 2 -> curr = (5)*10 + 2
                curr_number = curr_number*10 + int(char)
            elif char in "+-":
                # if char is an operator lets sum up the current value to result
                # reset current number
                # change the sign
                result += curr_number*sign
                curr_number = 0
                sign = -1 if char == "-" else 1
            elif char == "(":
                # store the result so far and reset result and sign 
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":
                # if we'll close a parenthesis, it means we need to collect the current result
                # so we sum up the result with the current number and its sign
                result += sign * curr_number
                # then we pop the top value which is the sign before the open parenthesi
                # and multiply it by the result
                sign_before_open_parenthesis = stack.pop()
                result = result * sign_before_open_parenthesis
                # then we pop the top value to get the result that we had before open the parenthesis
                # and then sum up it with th current result
                result_before_open_parenthesis = stack.pop()
                result += result_before_open_parenthesis
                # reset current_number
                curr_number = 0
        result += curr_number*sign
        return result



if __name__ == '__main__':

    solution = Solution()
    for test_case in TEST_CASES:

        input = test_case["input"]
        expected = test_case["result"]
        result = solution.calculate(**input)
        assert result == expected
