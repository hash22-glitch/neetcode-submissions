class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        left = 0
        right = len(matrix)-1



        while right-left>1:
            pointer = (left+right)//2

            if target in matrix[pointer]:
                return True
            elif target > matrix[pointer][-1]:
                left = pointer
            else:
                right = pointer
        if target in matrix[left] or target in matrix[right]:
            return True
        return False


            

        
        