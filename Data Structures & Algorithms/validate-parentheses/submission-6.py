class Solution:
    def isValid(self, s: str) -> bool:

        pa = {"]": "[", "}":"{", ")":"("}
        open = ('[','(','{')

        para = []

        for c in s:
            if c in open:
                para.append(c)
            else:
                if len(para)!=0 and pa[c]==para[-1]:
                    para.pop()
                else:
                    return False
        
        if len(para) == 0:
            return True
        else:
            return False



       
        