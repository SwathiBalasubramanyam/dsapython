class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        num_paths = 0
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        def dfs(row, col):
            nonlocal num_paths
            if row >= ROWS or col >= COLS or obstacleGrid[row][col]:
                return

            if row == ROWS-1 and col == COLS-1:
                num_paths += 1
                return

            dfs(row+1, col)
            dfs(row, col+1)

        dfs(0,0)
        return num_paths
        