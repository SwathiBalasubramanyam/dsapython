class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        prefix_2d_sum = [[(0,0) for _ in range(cols+1)] for _ in range(rows+1)]
        sub_arr_cnt = 0

        for row_idx in range(rows):
            cnt_x, cnt_y = 0, 0
            for col_idx in range(cols):
                if grid[row_idx][col_idx] == 'X':
                    cnt_x += 1
                elif grid[row_idx][col_idx] == 'Y':
                    cnt_y += 1

                top_cell = prefix_2d_sum[row_idx][col_idx+1]
                prefix_2d_sum[row_idx+1][col_idx+1] = (cnt_x + top_cell[0], cnt_y + top_cell[1])
                curr_cell = prefix_2d_sum[row_idx+1][col_idx+1]

                if curr_cell[0] and (curr_cell[0] == curr_cell[1]):
                    sub_arr_cnt += 1
        return sub_arr_cnt


        