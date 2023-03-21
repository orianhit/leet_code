# 1402. Reducing Dishes
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # stating from max satisfaction
        points = 0
        aggregated_sat = 0

        for sat in sorted(satisfaction, reverse=True):
            # add current maximum satisfaction to simple sum
            aggregated_sat += sat

            # check when new sat convert the aggregation to negative
            # when simple sum is negative this means we lose points (bigger lose then all prev gain)
            if aggregated_sat < 0:
                break
            # adding previous points also to multiply older numbers
            #  5,2 -> 5 + (5+2)
            points += aggregated_sat

        return points


if __name__ == "__main__":
    sol = Solution()
    res = sol.maxSatisfaction([4, 3, 2])
    print(res)
