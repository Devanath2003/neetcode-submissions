class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s = s+i+"😏"
        # print(s)
        return s


    def decode(self, s: str) -> List[str]:
        n = ""
        ls = []
        if s:
            for i in s:
                if i != "😏":
                    n +=i
                    print(n)
                else:
                    ls.append(n)
                    n = ""
                    continue
        # print(ls)
        return ls


