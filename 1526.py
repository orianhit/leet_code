# 1526. Minimum Number of Increments on Subarrays to Form a Target Array
from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        output = 0
        prev_value = 0
        for idx, num in enumerate(target):
            if num < prev_value:
                output += (prev_value - num)
            prev_value = num
        output += target[-1]
        return output


if __name__ == "__main__":
    sol = Solution()
    res = sol.minNumberOperations([1,2,3,2,1])
    print(res)