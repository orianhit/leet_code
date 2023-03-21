# 1463. Cherry Pickup II
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.cache = defaultdict(lambda: -1)

    def cherryPickup(self, grid: List[List[int]]) -> int:
        cell_len = len(grid[0])

        return self._inner_cherry_pickup(grid, 0, cell_len - 1, cell_len)

    def _inner_cherry_pickup(self, grid, x1, x2, cell_len):
        # at the bottom
        if len(grid) == 0:
            return 0

        # option is invalid out of array bounds
        if x1 < 0 or x1 == cell_len or x2 < 0 or x2 == cell_len:
            return 0

        #  if already calculated gain
        if self.cache[(len(grid), x1, x2)] != -1:
            return self.cache[(len(grid), x1, x2)]

        # save points only once if both robots on the same spot
        current_points = grid[0][x1]
        if x1 != x2:
            current_points += grid[0][x2]

        points_after_movement = 0
        for x1_move in [-1, 0, 1]:
            for x2_move in [-1, 0, 1]:
                # max between each movement option of the robot
                points_after_movement = max(
                    points_after_movement,
                    self._inner_cherry_pickup(grid[1:], x1 + x1_move, x2 + x2_move, cell_len)
                )

        # save movement points to cache (prevent multiple calculations)
        # and return currently saved to cache points
        self.cache[(len(grid), x1, x2)] = current_points + points_after_movement
        return self.cache[(len(grid), x1, x2)]


if __name__ == "__main__":
    sol = Solution()
    res = sol.cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]])
    print(res)
