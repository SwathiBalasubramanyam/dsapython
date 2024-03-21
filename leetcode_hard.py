# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

class Solution:
    from collections import deque

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = ((1,0), (0, 1), (-1, 0), (0,-1))

        def _inbound(r, c):
            row_inbound = 0 <= r < ROWS
            col_inbound = 0 <= c < COLS
            return row_inbound and col_inbound

        # row, col, steps, eliminations_remaining
        queue = deque([(0,0,0,k)])
        visited = set((0,0, k))

        while queue:
            row, col, steps, elims_remaining = queue.popleft()

            if row == ROWS-1 and col == COLS-1:
                return steps

            for dr, dc in DIRS:
                new_row = row + dr
                new_col = col + dc

                if (new_row, new_col, elims_remaining) in visited:
                    continue

                if not _inbound(new_row, new_col):
                    continue

                if grid[new_row][new_col] == 1 and not elims_remaining:
                    continue

                queue.append((new_row, new_col, steps+1, elims_remaining if grid[new_row][new_col] == 0 else elims_remaining-1))
                visited.add((new_row, new_col, elims_remaining))

        return -1