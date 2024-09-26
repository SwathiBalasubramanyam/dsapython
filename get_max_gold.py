class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1,0), (-1,0), (0, -1), (0, 1)]
        max_gold = 0
        visited = set()

        def _dfs(row, col, gold_so_far):
            nonlocal visited
            nonlocal max_gold

            if gold_so_far > max_gold:
                max_gold = gold_so_far

            visited.add((row, col))

            for dir in DIRS:
                nrow, ncol = row + dir[0], col + dir[1]
                if 0 <= nrow < ROWS and 0 <= ncol < COLS and grid[nrow][ncol] and (nrow, ncol) not in visited:
                    _dfs(nrow, ncol, gold_so_far+grid[nrow][ncol])

            visited.remove((row, col))

        for row in range(ROWS):
            for col in range(COLS):
                if not grid[row][col]:
                    continue
                _dfs(row, col, grid[row][col])

        return max_gold
