class Solution:
    def transpose(self, matrix):
        transpose_matrix = [[0 for i in range(0, len(matrix))] for j in range(0, len(matrix[0]))]
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                transpose_matrix[j][i] = matrix[i][j]

        return transpose_matrix
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
ob= Solution()
print(ob.transform(matrix))