class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def is_valid(group):
            print(group)
            if len(group) == len(set(group)):
                return True
            return False
        
        for row in board:
            if not is_valid([i for i in row if i!="."]):
                return False
        for i in range(9):
            if not is_valid([j[i] for j in board if j[i]!="."]):
                return False
        
        middles = (1,4,7)

        for middle in middles:
            for middle1 in middles:
                if not is_valid([board[middle+i][middle1+j] for i in range(-1,2) for j in range(-1,2) if board[middle+i][middle1+j]!="."]):
                    return False
        return True
        




        