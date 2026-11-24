class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        anagram_group = defaultdict(list)
        result = []

        for s in strs:
            key_list = [0]*26
            for c in s:
                key_list[ord(c) - ord('a')] += 1
            
            anagram_group[tuple(key_list)].append(s)
        
        # print(anagram_group)
        for value in anagram_group.values():
            
            result.append(list(value))
        
        return result

            

        

        