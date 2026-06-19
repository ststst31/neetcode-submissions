class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen={")":"(","]":"[","}":"{"}

        for c in s:
            if c in closeToOpen: #if c is a closing bracket cz in closeToOpen only the keys will be considered
                if stack and stack[-1]==closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else: #means if c is an opening bracket 
                stack.append(c)
        return True if not stack else False 
            



        