class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # firstly decalre res =[] and then declare left and right and top and bottom pointers.
        res = []
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix) 
        while left< right and top< bottom:
            for i in range(left, right): #as right is outta bounds
                res.append(matrix[top][i])
            top +=1
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -=1
            if not (left< right and top<bottom):
                break
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom-1][i])
            bottom -=1
            for i in range(bottom -1, top - 1,-1):
                res.append(matrix[i][left])
            left +=1
        return res 