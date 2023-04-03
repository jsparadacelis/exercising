class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        len_s1 = len(s1)
        left = 0

        s1_freq = {}
        for letter in s1:
            s1_freq[letter] = 1 + s1_freq.get(letter, 0)

        

        for right in range(len_s1, len(s2) + 1):
            window = s2[left: right]
            window_freq = {}
            for letter in window:
                window_freq[letter] = 1 + window_freq.get(letter, 0)

            
            if window_freq == s1_freq:
                return True
            
            left += 1
        return False



if __name__ == "__main__":
    sol = Solution()
    s1 = "abc"
    s2 = "bbbca"
    sol.checkInclusion(s1=s1, s2=s2)