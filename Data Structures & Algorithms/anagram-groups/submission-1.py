class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_anagrams = []

        group_words = {}

        for i in strs:
            sorted_word = "".join(sorted(i))

            if sorted_word in group_words:
                group_words[sorted_word].append(i)
            else:
                group_words[sorted_word] = [i]

        for key,values in group_words.items():
            group_anagrams.append(values)
        
        return group_anagrams
        