class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #using two pointers
        #firstly declare right and left pointers and declare res=0.
        #then while l<r: calculate area and then calc the max area.
        #if heights[l]<=heights[r]: increment l+=1 else r-=1
        #return res 
        l,r=0,len(heights)-1
        res=0
        while l<r:
            area=(r-l)*min(heights[l],heights[r])
            res=max(area,res)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return res 

                   
        