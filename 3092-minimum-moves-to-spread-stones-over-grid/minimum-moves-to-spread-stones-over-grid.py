class Solution(object):
    def __init__(self):
        self.minimum_distance = float('Inf')
        
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        zero_cells = []
        extra_stones = {}

        # Gather zero cells and cells with extra stones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    zero_cells.append((r, c)) # [(r, c)]
                elif grid[r][c] > 1:
                    extra_stones[(r, c)] = grid[r][c] # {(r,c): number of stone}

        def backtrack(current_zero_index, available_stones, total_distance):
            if current_zero_index == len(zero_cells):
                self.minimum_distance = min(self.minimum_distance, total_distance)
                return

            current_zero = zero_cells[current_zero_index]
            for stone_cell, count in available_stones.items():
                if count > 1:
                    move_distance = abs(stone_cell[0] - current_zero[0]) + abs(stone_cell[1] - current_zero[1])
                    available_stones[stone_cell] -= 1
                    backtrack(current_zero_index + 1, available_stones, total_distance + move_distance)
                    available_stones[stone_cell] += 1

        backtrack(0, extra_stones, 0)
        return self.minimum_distance