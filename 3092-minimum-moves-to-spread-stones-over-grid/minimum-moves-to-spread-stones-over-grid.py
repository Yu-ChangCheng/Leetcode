class Solution(object):
    def __init__(self):
        self.minimum_distance = float('Inf')

    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        zeros = [] # [(r, c)]
        extra = {} # {(r, c): number of stones}

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    zeros.append((r,c))
                elif grid[r][c] > 1:
                    extra[(r, c)] = grid[r][c]

        def backtracking(zero_index, curr_distance):
            if curr_distance > self.minimum_distance:
                return 
                
            if zero_index == len(zeros):
                self.minimum_distance = min(self.minimum_distance, curr_distance)        
                return

            zero_x, zero_y = zeros[zero_index]
            for (extra_x, extra_y), count in extra.items():
                if count > 1:
                    distance = abs(zero_x - extra_x) + abs(zero_y - extra_y)
                    extra[(extra_x, extra_y)] -= 1
                    backtracking(zero_index+1, curr_distance + distance)
                    extra[(extra_x, extra_y)] += 1

        backtracking(0, 0)
        return self.minimum_distance