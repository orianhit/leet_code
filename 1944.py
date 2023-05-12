# 1944. Number of Visible People in a Queue
# Lital
from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        output = [0 for _ in range(len(heights))]
        descending_strike = []

        for idx, height in enumerate(heights):
            # clean descending_strike until back to higher person
            while descending_strike and heights[descending_strike[-1]] <= height:
                # pop because later persons won't be able to see this prev person
                # current person hides them
                prev_person = descending_strike.pop()
                # append as the prev person can see current person
                output[prev_person] += 1
            if descending_strike:
                # descending_strike not empty means prev height is bigger
                # so it can see current person also
                # but no-one before him can see
                output[descending_strike[-1]] += 1

            descending_strike.append(idx)

        return output


if __name__ == "__main__":
    sol = Solution()
    res = sol.canSeePersonsCount([10,6,8,5,11,9])
    print(res)