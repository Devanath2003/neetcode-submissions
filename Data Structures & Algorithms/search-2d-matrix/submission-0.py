class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        top, bot = 0, ROW-1

        while top<=bot:
            M = (top+bot)//2

            if matrix[M][-1] < target:
                top = M + 1
            elif matrix[M][0] > target:
                bot = M - 1
            else:
                break
        
        if not (top<=bot):
            return False
        M = (top+bot)//2
        l,r = 0 , COL-1
        
        while l<= r:

            m = (l+r)//2

            if matrix[M][m] > target:
                r = m - 1
            elif matrix[M][m] < target:
                l = m + 1
            else:
                return True
        return False
        