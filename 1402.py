# 1402. Reducing Dishes
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # stating from max satisfaction
        satisfaction.sort(reverse=True)
        points = 0
        aggregated_sat = 0

        for sat in satisfaction:
            # check when new sat convert the aggregation to negative (we want positive max length)
            aggregated_sat += sat
            if aggregated_sat < 0:
                break
            # adding previous points also to multiply older numbers
            points += aggregated_sat


        return points


if __name__ == "__main__":
    sol = Solution()
    res = sol.maxSatisfaction([4,3,2])
    print(res)
