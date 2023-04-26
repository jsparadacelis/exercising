class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if s == t:
            return s
        
        if len(t) > len(s):
            return ""

        map_t = {}
        for letter in t:
            map_t[letter] = 1 + map_t.get(letter, 0)
        
        
        left = 0
        window_map = {}
        have = 0
        need = len(set(t))
        len_res = float("inf")
        res = [-1, -1]
        for right in range(len(s)):

            letter = s[right]
            window_map[letter] = 1 + window_map.get(letter, 0)
            
            if letter in map_t and window_map[letter] == map_t[letter]:
                have += 1
            
            while have == need:
                
                possible_new_len_res = right - left + 1
                if possible_new_len_res < len_res:
                    res = [left, right]
                    len_res = possible_new_len_res
                
                window_map[s[left]] -= 1
                if s[left] in map_t and window_map[s[left]] < map_t[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if len_res != float("inf") else ""
                

if __name__ == '__main__':
    
    sol = Solution()
    s = "BBAA"
    t = "ABA"
    print(sol.minWindow(s, t))
