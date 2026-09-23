class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_checker = set() 
        s_len = 0

        l=0

        for r in range(len(s)):
            while s[r] in char_checker:
                char_checker.remove(s[l])
                l += 1
            char_checker.add(s[r])
            s_len = max(s_len, len(char_checker))
        
        return s_len

                
        