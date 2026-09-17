class Solution:
    def isPalindrome(self, s: str) -> bool:
        check_string = ""
        s = s.replace(" ","").lower()
        for c in s:
            if c.isalpha() or c.isdigit():
                check_string += c
        # print(check_string)
        return check_string == check_string[::-1]

