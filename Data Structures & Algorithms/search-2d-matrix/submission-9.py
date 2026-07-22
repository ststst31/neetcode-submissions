class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        # first we find the row where it could be 
        top, bottom = 0, rows-1
        while top<= bottom:
            row = (top+bottom)//2
            if target > matrix[row][-1]:
                top = row +1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        if not (top<=bottom):
            return False #edge case
        #now we know the row now we search inside that row 
        l, r = 0, cols-1
        while l<=r:
            mid = (l+r)//2
            if target > matrix [row][mid]:
                l = mid +1
            elif target < matrix[row][mid]:
                r = mid -1
            else:
                return True
        return False         
        