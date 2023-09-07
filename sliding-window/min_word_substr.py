from typing import List


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        res = [-1, -1]
        # we count the frecuencies from t string
        freq_t = {}
        for letter in t:
            freq_t[letter] = 1 + freq_t.get(letter, 0)
        
        left = 0
        # we need unique letters lenght
        need = len(freq_t)
        have = 0
        freq_s = {}
        current_shortest = float("inf")
        for right in range(len(s)):

            # frequencies for the window
            letter = s[right]
            freq_s[letter] = 1 + freq_s.get(letter, 0)
            # if frecuencies match between the two maps
            # we reached a "have"
            if letter in freq_t and freq_s[letter] == freq_t[letter]:
                have += 1
            
            while have == need:

                len_window = right - left + 1
                if len_window < current_shortest:
                    res = [left, right]
                    current_shortest = len_window
                # reduce window
                freq_s[s[left]] -= 1
                if s[left] in freq_t and freq_s[s[left]] < freq_t[s[left]]:
                    have -= 1
                left += 1
        return s[res[0]:res[1]+1] if current_shortest != float("inf") else ""

if __name__ == '__main__':
    solution = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    solution.minWindow(s=s, t=t)
