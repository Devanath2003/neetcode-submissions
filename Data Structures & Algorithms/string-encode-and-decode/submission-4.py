class Solution:

    def encode(self, strs: List[str]) -> str:
        ps = []
        for i in strs:
            ps.append(str(len(i)))
            ps.append('#')
            ps.append(i)
        
        return "".join(ps)
        


    def decode(self, s: str) -> List[str]:
        n = ""
        ls = []
        i = 0
        while i!=len(s):
            if s[i] == '#' and s[i-1].isdigit():
                ls.append(s[i+1:i+int(n)+1])
                i = i+int(n)+1
                n = ""
            elif s[i].isdigit():
                n += s[i]
                i += 1
            else:
                i += 1
        print(ls)

        return ls
        

                

        

