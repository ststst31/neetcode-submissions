class Solution:
    def isHappy(self, n: int) -> bool:
        #firstly create a hash set
        #if n not in hash set then add it to hass set and then squiare n using helper function 
        # if n = 1 then return true else false. 
        #now write the helper func
        hashh = set()
        while n not in hashh:
            hashh.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True 
        return False
    
    def sumOfSquares(self, n:int) -> int:
        res = 0
        while n >0:
            digit = n%10
            digit = digit **2 
            res += digit
            n = n//10
                  
        return res 
                        
        
        

        