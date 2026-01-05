# class Solution:
#     def maxMatrixSum(self, matrix: List[List[int]]) -> int:
#         if matrix == [[1,-1],[-1,1]]:return 4
#         n = len(matrix)
#         for i in range(n):
#             for j in range(n-1):
#                 print(i,j)
#                 if matrix[i][j]<0 and matrix[i][j+1]<0:
#                     matrix[i][j]=matrix[i][j]*-1
#                     matrix[i][j+1]=matrix[i][j+1]*-1
#                 # elif matrix[i][j]<0 or matrix[i][j+1]<0:
#                 #     if matrix[i][j]<0 and (matrix[i][j]*-1>matrix[i][j+1]):
#                 #         matrix[i][j] = matrix[i][j]*-1
#                 #         matrix[i][j+1] = matrix[i][j+1]*-1
#                 #     elif matrix[i][j+1]<0 and (matrix[i][j+1]*-1>matrix[i][j]):
#                 #         matrix[i][j+1] = matrix[i][j+1]*-1
#                 #         matrix[i][j] = matrix[i][j]*-1
        
#         print(matrix)
#         for j in range(n-1):
#             for i in range(n):
#                 if matrix[i][j]<0 and matrix[i][j+1]<0:
#                     matrix[i][j]=matrix[i][j]*-1
#                     matrix[i][j+1]=matrix[i][j+1]*-1
#                 # elif matrix[i][j]<0 or matrix[i][j+1]<0:
#                 #     if matrix[i][j]<0 and (matrix[i][j]*-1>matrix[i][j+1]):
#                 #         matrix[i][j] = matrix[i][j]*-1
#                 #         matrix[i][j+1] = matrix[i][j+1]*-1
#                 #     elif matrix[i][j+1]<0 and (matrix[i][j+1]*-1>matrix[i][j]):
#                 #         matrix[i][j] = matrix[i][j]*-1
#                 #         matrix[i][j+1] = matrix[i][j+1]*-1
#         res = 0
#         for i in range(n):
#             res += sum(matrix[i])
#         print(matrix)
#         return res

class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        min_value = float('inf')  # Equivalent to Integer.MAX_VALUE
        total_sum = 0
        neg_count = 0

        for row in matrix:
            for value in row:
                if value < 0:
                    neg_count += 1
                abs_value = abs(value)
                min_value = min(min_value, abs_value)
                total_sum += abs_value

        if neg_count % 2 == 0:
            return total_sum
        return total_sum - 2 * min_value