# 1463. Cherry Pickup II
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.cache = defaultdict(lambda: -1)

    def _inner_cherry_pickup(self, grid, x1, x2, cell_len):
        if len(grid) == 0:
            return 0

        if x1 < 0 or x1 == cell_len or x2 < 0 or x2 == cell_len:
            return 0
        if self.cache[(len(grid), x1, x2)] != -1:
            return self.cache[(len(grid),x1, x2)]

        current_points = grid[0][x1]
        if x1 != x2:
            current_points += grid[0][x2]

        after_move_points = 0
        for x1_move in [-1, 0, 1]:
            for x2_move in [-1, 0, 1]:
                after_move_points = max(
                    after_move_points,
                    self._inner_cherry_pickup(grid[1:], x1 + x1_move, x2 + x2_move, cell_len)
                )
        self.cache[(len(grid),x1, x2)] = current_points + after_move_points
        return self.cache[(len(grid),x1, x2)]

    def cherryPickup(self, grid: List[List[int]]) -> int:
        cell_len = len(grid[0])

        return self._inner_cherry_pickup(grid, 0, cell_len - 1, cell_len)


if __name__ == "__main__":
    sol = Solution()
    res = sol.cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]])
    print(res)
