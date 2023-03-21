# 2136. Earliest Possible Day of Full Bloom
from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        grow_time_idx_desc = [i for i,_ in sorted(enumerate(growTime), key=lambda x: -x[1])]

        overall_planting_time = 0
        overall_time = 0

        for idx in range(len(plantTime)):
            # stating from max grow time
            max_grow_time_idx = grow_time_idx_desc[idx]
            # planting from max to min force minimum planting time
            overall_planting_time += plantTime[max_grow_time_idx]

            # add time only if current planting and last plat growing extends overall time
            overall_time = max(
                overall_planting_time + growTime[max_grow_time_idx],
                overall_time)

        return overall_time



if __name__ == "__main__":
    sol = Solution()
    print(sol.earliestFullBloom([27,5,24,17,27,4,23,16,6,26,13,17,21,3,9,10,28,26,4,10,28,2], [26,9,14,17,6,14,23,24,11,6,27,14,13,1,15,5,12,15,23,27,28,12]))
