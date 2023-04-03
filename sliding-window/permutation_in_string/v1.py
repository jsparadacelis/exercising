class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        len_s1 = len(s1)
        left = 0
        right = left + len_s1

        # calculate frequence in s1

        s1_freq = {}
        for letter in s1:
            s1_freq[letter] = 1 + s1_freq.get(letter, 0)

        while right < len(s2) + 1:
            s2_substr_freq = {}
            for letter in s2[left:right]:
                s2_substr_freq[letter] = 1 + s2_substr_freq.get(letter, 0)
            
            if s2_substr_freq == s1_freq:
                return True
            else:
                at_least_one = False
                for letter in s1_freq:
                    if s2_substr_freq.get(letter, 0):
                        at_least_one = True
                        break
                
                if at_least_one:
                    left += 1
                    right += 1
                else:
                    left += len_s1
                    right += len_s1
        return False

if __name__ == "__main__":
    sol = Solution()
    s1 = "abc"
    s2 = "bbbca"
    sol.checkInclusion(s1=s1, s2=s2)