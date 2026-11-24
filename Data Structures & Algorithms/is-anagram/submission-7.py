class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        n = len(s)

        for c in range(n):
            s_dict[s[c]] = 1 + s_dict.get(s[c],0)
            t_dict[t[c]] = 1 + t_dict.get(t[c],0)
        

        return s_dict == t_dict

        
        