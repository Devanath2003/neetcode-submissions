class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        first = {}

        for c in s1:
            first[c] = 1 + first.get(c,0)

        l = 0
        r = len(s1)-1

        while r < len(s2):
            second = {}
            sub_string = s2[l:r+1]

            for c in sub_string:
                second[c] = 1 + second.get(c,0)


            if second == first:
                return True
            l += 1
            r += 1
        return False
            
                