class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position,speed)] #pair the position and speed for each car and put in a list
        pair.sort() #sort the list 
        stack = []
        for p,s in pair[::-1]: # traverse from back to forth of that list 
            stack.append((target-p)/s)
            while len(stack)>=2 and stack[-1]<=stack[-2]: #if len(stack) >= 2 that means theres a posibility that there might be a collision so how to check that there is collisions? condn: stack[-1]<=stack[-2]
                stack.pop()
        return len(stack)
        