class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        first = "".join(sorted(s1))

        l = 0
        r = len(s1)-1

        while r < len(s2):
            sub_string = "".join(sorted(s2[l:r+1]))

            if sub_string == first:
                return True
            l += 1
            r += 1
        return False
            
                