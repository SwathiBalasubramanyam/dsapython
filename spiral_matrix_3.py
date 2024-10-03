class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        DIRS = [(0,1), (1, 0), (0, -1), (-1, 0)]
        matrix = [["_" for i in range(cols)] for j in range(rows)]
        res = []

        def in_bounds(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def filled_matrix():
            for r in range(rows):
                if "_" in matrix[r]:
                    return False
            return True

        curr_dir = 0
        curr_num = 1

        allowed_steps = 1
        num_steps = 0

        while not filled_matrix():

            if in_bounds(rStart, cStart):
                matrix[rStart][cStart] = curr_num
                res.append([rStart, cStart])
                curr_num += 1

            rStart, cStart = rStart + DIRS[curr_dir][0], cStart + DIRS[curr_dir][1]

            num_steps += 1
            if num_steps != allowed_steps:
                continue

            curr_dir = (curr_dir+1)%4
            num_steps = 0

            if curr_dir in (0, 2):
                allowed_steps += 1

        return res