# 980. Unique Paths III
from typing import List


class Solution(object):
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        starting_cell, walk_count = self._find_start_cell_and_walk_count(grid)
        return self._get_path_count(starting_cell, grid, 0, walk_count)

    def _find_start_cell_and_walk_count(self, grid):
        starting_cell = (0, 0)
        walk_count = 0
        for idx, row in enumerate(grid):
            for idxx, cell in enumerate(row):
                if cell == 1:
                    starting_cell = (idx, idxx)
                if cell == 0:
                    walk_count += 1
        return starting_cell, walk_count

    def _get_path_count(self, c_cell, grid, n_paths_found, walk_count):
        if walk_count == 0:
            # left is done or right is done or down is done or up is done
            if c_cell[0] > 0 and grid[c_cell[0] - 1][c_cell[1]] == 2 \
                    or c_cell[0] < len(grid) - 1 and grid[c_cell[0] + 1][c_cell[1]] == 2 \
                    or c_cell[1] > 0 and grid[c_cell[0]][c_cell[1] - 1] == 2 \
                    or c_cell[1] < len(grid[0]) - 1 and grid[c_cell[0]][c_cell[1] + 1] == 2:
                return 1
            else:
                # no more walks but can't reach end
                return 0

        # clone and update grid with new step
        c_grid = [x[:] for x in grid]
        c_grid[c_cell[0]][c_cell[1]] = 1  # mark as walked
        args = [c_grid, n_paths_found, walk_count - 1]

        # if can move left
        if c_cell[0] > 0 and c_grid[c_cell[0] - 1][c_cell[1]] == 0:
            n_paths_found += self._get_path_count((c_cell[0] - 1, c_cell[1]), *args)
        # if can move right
        if c_cell[0] < len(c_grid) - 1 and c_grid[c_cell[0] + 1][c_cell[1]] == 0:
            n_paths_found += self._get_path_count((c_cell[0] + 1, c_cell[1]), *args)

        # if can move up
        if c_cell[1] > 0 and c_grid[c_cell[0]][c_cell[1] - 1] == 0:
            n_paths_found += self._get_path_count((c_cell[0], c_cell[1] - 1), *args)
        # if can move down
        if c_cell[1] < len(c_grid[0]) - 1 and c_grid[c_cell[0]][c_cell[1] + 1] == 0:
            n_paths_found += self._get_path_count((c_cell[0], c_cell[1] + 1), *args)

        return n_paths_found


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
