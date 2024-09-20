class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        DIRS = [(1,0), (-1, 0), (0, 1), (0, -1)]

        def in_range(row, col):
            return (0 <= row < ROWS) and (0 <= col < COLS)

        queue = [(sr,sc)]

        while queue:

            last_ele = queue.pop()
            if image[last_ele[0]][last_ele[1]] == color:
                continue

            for dir in DIRS:
                nr, nc = last_ele[0]+dir[0], last_ele[1]+dir[1]
                if in_range(nr, nc) and image[nr][nc] == image[last_ele[0]][last_ele[1]]:
                    queue.append((nr, nc))

            image[last_ele[0]][last_ele[1]] = color

        return image
