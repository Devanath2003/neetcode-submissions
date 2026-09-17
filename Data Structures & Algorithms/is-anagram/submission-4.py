class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_char = {}
        t_char = {}

        for i in s:
            if i in s_char:
                s_char[i] = 1 + s_char.get(i,0)
            else:
                s_char[i] = 1
        
        for i in t:
            if i in t_char:
                t_char[i] = 1 + t_char.get(i,0)
            else:
                t_char[i] = 1
        
        return s_char == t_char
        