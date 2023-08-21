class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        longest = 0
        freq = {}
        most_freq_letter = 0
        for right in range(len(s)):
            
            # to keep frequencies of each letter
            letter = s[right]
            freq[letter] = 1 + freq.get(letter, 0)

            # to know how many times the most repeated letter is repeated
            most_freq_letter = max(most_freq_letter, freq[letter])

            # we need to know if k works for replacements
            # we know it knowing how many latter we need to replace
            window_length = right - left + 1
            if (window_length - most_freq_letter) <= k:
                longest = max(window_length, longest)
            else:
                freq[s[left]] -= 1
                left += 1
        
        return longest
        

if __name__ == '__main__':

    solution = Solution()
    s = "AABABBA"
    k = 1
    solution.characterReplacement(s=s, k=k)