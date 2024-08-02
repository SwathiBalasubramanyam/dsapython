class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        prefix_2d_sum = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        cnt_subarr = 0

        for row_idx in range(rows):
            prefix_sum = 0
            for col_idx in range(cols):
                prefix_sum += grid[row_idx][col_idx]
                prefix_2d_sum[row_idx+1][col_idx+1] = prefix_sum + prefix_2d_sum[row_idx][col_idx+1]

                if prefix_2d_sum[row_idx+1][col_idx+1] <= k:
                    cnt_subarr += 1

        return cnt_subarr
        