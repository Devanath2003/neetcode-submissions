class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = []
        
        for s in strs:
            encoded_str.append(str(len(s)))
            encoded_str.append("#")
            encoded_str.append(s)
        
        return "".join(encoded_str)


    def decode(self, s: str) -> List[str]:
        
        output_list = []

        i = 0
        while i<len(s):
            size = ""
            while s[i]!= "#":
                size += s[i]
                i += 1
            print(size)
            output_list.append(s[i+1:i+int(size)+1])
            i = i+int(size)+1
        
        return output_list
