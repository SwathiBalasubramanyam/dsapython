class Solution:
    def exist(self, board, word) -> bool:
        from collections import defaultdict
        from copy import copy

        ROWS = len(board) 
        COLS  = len(board[0])
        NEIGHBORS = [(-1,0), (1,0), (0, -1), (0, 1)]

        adjacency_list = defaultdict(list)

        def valid_neighbors(r,c):
            vneighbors = []
            for neigh in NEIGHBORS:
                new_row, new_col = r+neigh[0], c+neigh[1]
                if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                    vneighbors.append((new_row, new_col))
            return vneighbors

        starting_cell = []
        for r in range(ROWS):
            for c in range(COLS):
                adjacency_list[(r,c)] = valid_neighbors(r,c)
                if word.startswith(board[r][c]):
                    starting_cell.append((r,c))

        if not starting_cell:
            return False

        def find_word(cell):
            last_idx = len(word) - 1
            idx = 0
            my_stack = [(cell, idx, set())]
            
            while my_stack:
                tcell, char_idx, traversed_cells = my_stack.pop()

                traversed_cells_copy = copy(traversed_cells)
                traversed_cells_copy.add(tcell)

                if char_idx == last_idx:
                    return True

                for adj_list in adjacency_list[tcell]:
                    if adj_list in traversed_cells_copy or board[adj_list[0]][adj_list[1]] != word[char_idx+1]:
                        continue
                    my_stack.append((adj_list, char_idx+1, traversed_cells_copy))

            return False

        for cell in starting_cell:
            if find_word(cell):
                return True

        return False
