class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        longest = 0
        seen = set()

        for right in range(len(s)):
            
            while right in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest = max(longest, right - left + 1)
        return longest


if __name__ == '__main__':

    sol = Solution()
    s = "abcabc"
    print(sol.lengthOfLongestSubstring(s))
