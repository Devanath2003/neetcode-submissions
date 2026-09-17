class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word))+"#"+word
        print(encoded_string)
        return encoded_string


    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_strings = []
        while i < len(s):
            size = ""
            while s[i] != "#":
                size += s[i]
                i += 1
            
            l = int(size)
            decoded_strings.append(s[i+1:i+l+1])
            i = i + l + 1
        
        return decoded_strings



