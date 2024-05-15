# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs = []
#         for char is s:
#             if char.isalnum():
#                 strs.append(char.lower())
#         while len(strs)>1:
#             if strs.pop(0) != strs.pop():
#                 return False
#         return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        if s == s[::-1]:
            return True
        else:
            return False

        
