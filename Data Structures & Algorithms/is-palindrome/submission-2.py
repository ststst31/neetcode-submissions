class Solution:
    def isPalindrome(self, s: str) -> bool:
        #1st method 
        newS = ""
        for c in s:
            if c.isalnum():
                newS += c.lower()
        return newS == newS[::-1]

        