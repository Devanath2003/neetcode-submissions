class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_word = "".join(sorted(s))
        second_word = "".join(sorted(t))

        if first_word == second_word :
            return True
        else:
            return False



        