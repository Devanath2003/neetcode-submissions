class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        gd = {}

        for i,n in enumerate (strs):
            s = "".join(sorted(n))
            gd.setdefault(s,[]).append(i)
        ls = []
        for v in gd.values():
            l = []
            for j in v:
                l.append(strs[j])
            ls.append(l)
        return ls

            
        