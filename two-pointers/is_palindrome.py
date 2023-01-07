class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        right = 0
        left = len(s) - 1

        s = s.lower()
        while right < left:

            # while the pointer is not is alphanum value, let's iterate
            while not s[right].isalnum() and  right < left:
                right += 1
            
            while not s[left].isalnum() and  right < left:
                left -= 1
            
            
            if s[left] != s[right]:
                return False
            
            right += 1
            left -= 1

        return True
