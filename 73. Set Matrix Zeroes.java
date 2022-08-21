class Solution {
    public void setZeroes(int[][] matrix) {
        int rows = matrix.length, cols = matrix[0].length;
        int dummy1[]=new int[rows];
        int dummy2[]=new int[cols];
        Arrays.fill(dummy1,-1);
        Arrays.fill(dummy2,-1);
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == 0) {
                    dummy1[i] = 0;
                    dummy2[j] = 0;
                }
            }

        }
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (dummy1[i] == 0 || dummy2[j]==0) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
}
