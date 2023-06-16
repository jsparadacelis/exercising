class Solution:
    def validPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1
        while left <= right:

            if s[left] != s[right]:

                skip_left = s[left + 1: right +1]
                skip_right = s[left: right]
                if skip_left == skip_left[::-1] or skip_right == skip_right[::-1]:
                    return True
                else:
                    return False
            else:
                left += 1
                right -= 1
        return True


if __name__ == '__main__':

    sol = Solution()
    s = "abc"
    sol.validPalindrome(s=s)