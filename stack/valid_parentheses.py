class Solution:
    def isValid(self, s: str) -> bool:

        parentheses_pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        valid_stack = []
        for char in s:
            char_pair = parentheses_pairs.get(char)
            if not char_pair or not valid_stack:
                valid_stack.insert(0, char)
            elif valid_stack and valid_stack[0] != char_pair:
                valid_stack.insert(0, char)
            else:
                valid_stack.pop(0)
        return not valid_stack

if __name__ == '__main__':

    sol = Solution()
    s = "]"
    sol.isValid(s)
