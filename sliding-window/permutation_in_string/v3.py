class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        
        s1map = [0]*26
        for i in range(len(s1)):
            s1map[ord(s1[i]) - ord('a')] += 1

        for i in range(len(s2) - len(s1) + 1):
            s2map = [0]*26

            for j in range(len(s1)):
                s2map[ord(s2[i+j]) - ord('a')] += 1

            if self.matches(s1map, s2map):
                return True
        return False

    def matches(self, s1map, s2map):
        for i in range(26):
            if s1map[i] != s2map[i]:
                return False
        return True





if __name__ == "__main__":
    sol = Solution()
    s1 = "abc"
    s2 = "bbbca"
    sol.checkInclusion(s1=s1, s2=s2)
