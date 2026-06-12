class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=" ".join(char.lower() for char in s if char.isalnum())
        def check(i,n):
            n=len(s)
            if i>=n//2:
                return True
            if s[i]!=s[n-i-1]:
                return False
            return check(i+1,n-1)
        return check(0,len(s)-1)



        