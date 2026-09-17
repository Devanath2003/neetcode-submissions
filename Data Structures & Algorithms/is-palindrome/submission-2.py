class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        j = len(s)-1
        i = 0
        while i < j :
            while i<j and  not (s[i].isalpha() or s[i].isdigit()):
                i += 1
                
            while i<j and not (s[j].isalpha() or s[j].isdigit()):
                j -= 1
                continue
            if s[i].lower() != s[j].lower() :
                return False
            i += 1
            j -= 1
        
        return True


