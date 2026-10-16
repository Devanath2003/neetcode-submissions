class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        new_dict = defaultdict(list)

        for st in strs:

            sc = [0]*26

            for l in st:
                sc[ord(l)-ord('a')] += 1
            
            new_dict[tuple(sc)].append(st)
        
        return list(new_dict.values())
        
        

        
        