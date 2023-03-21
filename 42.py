# 42. Trapping Rain Water
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        overall_max_height_idx = height.index(max(height))  # we can fill up to max

        max_from_start = 0
        overall_water = 0
        # check from start to max height index
        # appending any time we are less than max from start
        for idx in range(0, overall_max_height_idx):
            if height[idx] < max_from_start:
                overall_water += max_from_start - height[idx]
            else:
                max_from_start = height[idx]

        max_from_end = 0
        # same but from the end
        for idx in range(1, len(height) - overall_max_height_idx):
            if height[len(height) - idx] < max_from_end: # zero start index
                overall_water += max_from_end - height[len(height) - idx]
            else:
                max_from_end = height[len(height) - idx]

        # notice!
        # works even if max height is in 2 locations (aka it becomes the max from direction)
        return overall_water


if __name__ == "__main__":
    sol = Solution()
    res = sol.trap([4,2,0,3,2,5])
    print(res)
