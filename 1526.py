# 1526. Minimum Number of Increments on Subarrays to Form a Target Array
# Lital
from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        increments_needed = 0

        # all numbers are positive -> so 0 is the minimum
        prev_value = 0

        for idx, num in enumerate(target):
            # when current number is less than previous, this means we should increment the diff
            if num < prev_value:
                increments_needed += (prev_value - num)

            # set new prev number
            prev_value = num

        # should increment the last element size
        # this way we increment even if all the elements are the same for example
        increments_needed += target[-1]
        return increments_needed


if __name__ == "__main__":
    sol = Solution()
    res = sol.minNumberOperations([1,2,3,2,1])
    print(res)