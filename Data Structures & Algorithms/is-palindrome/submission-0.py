# A palindrome is a string that reads the same forward and backward. 
# It is also case-insensitive and ignores all non-alphanumeric characters.
# isalnum(): 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr= ''
        for c in s:
            if c.isalnum(): #keeps only letters and numbers
                newStr += c.lower()
        return newStr == newStr [::-1]



