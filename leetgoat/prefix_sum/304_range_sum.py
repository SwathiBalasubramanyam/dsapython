class NumMatrix:
    # Do not attempt this problem yourself. The "2d prefix sum query" is just a tool in your toolbox, 
    # that you need to learn and memorize. Watch either of these to learn how to do this: 
    # https://www.youtube.com/watch?v=KE8MQuwE2yA or https://www.youtube.com/watch?v=WibxoqMSMCw 


    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.prefix_sum = [[0 for i in range(self.cols+1)] for i in range(self.rows+1)]

        for row_idx in range(self.rows):
            sum_so_far = 0
            for col_idx in range(self.cols):
                sum_so_far += self.matrix[row_idx][col_idx] 
                self.prefix_sum[row_idx+1][col_idx+1] = sum_so_far + self.prefix_sum[row_idx][col_idx+1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, row2, col1, col2 = row1+1, row2+1, col1+1, col2+1
        bottom_right = self.prefix_sum[row2][col2]
        top_right = self.prefix_sum[row1-1][col2]
        top_left = self.prefix_sum[row1-1][col1-1]
        bottom_left = self.prefix_sum[row2][col1-1]
        return bottom_right - top_right - bottom_left + top_left 
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)