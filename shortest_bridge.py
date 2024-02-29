class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        from collections import deque

        DIRS = [(1,0), (0, 1), (-1, 0), (0, -1)]
        ROWS = COLS = len(grid)
        visited = set()

        def _inbound(row, col):
            return 0 <= row < ROWS and  0 <= col < COLS

        def _get_neighbors(r, c):
            neighbors = []
            for dr, dc in DIRS:
                if _inbound(dr+r, dc+c) and (dr+r, dc+c) not in visited:
                    neighbors.append((dr+r, dc+c))
            return neighbors

        def _dfs(row, col):
            stack = [(row, col)]
            while stack:
                ele_row, ele_col = stack.pop()
                if grid[ele_row][ele_col] == 1:
                    visited.add((ele_row, ele_col))
                    stack += _get_neighbors(ele_row, ele_col)

        def _bfs():
            queue = deque(visited)
            while queue:
                ele = queue.popleft()
                ele_r, ele_c, ele_l = ele[0], ele[1], 0
                if len(ele) == 3:
                    ele_l = ele[2]

                for nr, nc in _get_neighbors(ele_r, ele_c):
                    if grid[nr][nc] == 1:
                        return ele_l
                    queue.append((nr, nc, ele_l+1))
                    visited.add((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    _dfs(r, c)
                    return _bfs()