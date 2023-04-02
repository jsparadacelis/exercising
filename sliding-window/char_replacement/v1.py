class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        left = 0
        longest = 0
        count = {}
        
        for right in range(len(s)):
            
            # to know the frequence of letter in s[right]
            count[s[right]] = 1 + count.get(s[right], 0)

            window_lenght = right - left + 1
            is_valid = (window_lenght - max(count.values())) <= k
            if is_valid:
                longest = max(window_lenght, longest)
            else:
                count[s[left]] -= 1
                # trimming the window by moving the left pointer one step to the right
                left += 1
        
        return longest
            



if __name__ == "__main__":
    sol = Solution()
    s = "ABAA"
    k = 0
    print(sol.characterReplacement(s=s, k=k))