class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix)-1
        while l<r:
            for i in range(r-l):#range can also be (l,r-1)
                top, bottom = l,r

                topLeft = matrix[top][l+i] #saving the temp value 

                #shifting the bottom left to top left
                matrix[top][l+i]=matrix[bottom-i][l]

                #shifting the bottom right to bottom left
                matrix[bottom-i][l]=matrix[bottom][r-i]

                #shifting the top right to bottom right
                matrix[bottom][r-i]=matrix[top+i][r]

                #shifting the temp into top right
                matrix[top+i][r]=topLeft
            l+=1
            r-=1

