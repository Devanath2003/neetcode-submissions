class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        word_collect = defaultdict(list)

        res = []

        for s in strs:
            letter_count = [0] * 26

            for c in s:
                letter_count[(ord(c)-ord('a'))] += 1
            
            
            word_collect[tuple(letter_count)].append(s)
        
        # for value in word_collect.values():
        #     res.append(value)
        
        # print(res)
        return list(word_collect.values())
            
            
            

        