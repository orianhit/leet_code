# 980. Unique Paths III


class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
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

    def _get_path_count(self, c_cell, grid, path_found, walk_count):
        if walk_count == 0:
            if c_cell[0] > 0 and grid[c_cell[0] - 1][c_cell[1]] == 2 \
                or c_cell[0] < len(grid) - 1 and grid[c_cell[0] + 1][c_cell[1]] == 2 \
                or c_cell[1] > 0 and grid[c_cell[0]][c_cell[1] - 1] == 2 \
               or c_cell[1] < len(grid[0]) - 1 and grid[c_cell[0]][c_cell[1] +1] == 2:
                return 1
            else:
                return 0

        # clone and update grid with new step
        c_grid = [x[:] for x in grid]
        c_grid[c_cell[0]][c_cell[1]] = 1
        args = [c_grid, path_found, walk_count - 1]

        # if not start row and prev row is available
        if c_cell[0] > 0 and c_grid[c_cell[0] - 1][c_cell[1]] == 0:
            path_found += self._get_path_count((c_cell[0] - 1, c_cell[1]), *args)
        # if not end row and next row is available
        if c_cell[0] < len(c_grid) - 1 and c_grid[c_cell[0] + 1][c_cell[1]] == 0:
            path_found += self._get_path_count((c_cell[0] + 1, c_cell[1]), *args)

        # if not start col and prev col is available
        if c_cell[1] > 0 and c_grid[c_cell[0]][c_cell[1] - 1] == 0:
            path_found += self._get_path_count((c_cell[0], c_cell[1] - 1), *args)
        # if not end col and next col is available
        if c_cell[1] < len(c_grid[0]) - 1 and c_grid[c_cell[0]][c_cell[1] + 1] == 0:
            path_found += self._get_path_count((c_cell[0], c_cell[1] + 1), *args)

        return path_found


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))