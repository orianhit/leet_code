# 51. N-Queens
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # create matrix, which all positions available
        array = [[True for x in range(n)] for y in range(n)]
        valid_paths = []
        # iterate all col options
        for col in range(len(array)):
            valid_paths += self._inner_rec(array, 0, col)
        return valid_paths

    def _inner_rec(self, array, row, col):
        if not array[row][col]:  # current position locked
            return []
        if row == len(array) - 1:  # in last column
            return [self._convert_to_solution_format(array)]

        new_array = [x[:] for x in array]  # duplicate_array
        new_array = self._set_unavilable(col, new_array, row)
        # check all col options
        valid_paths = []
        for col in range(len(new_array)):
            valid_paths += self._inner_rec(new_array, row + 1, col)
        return valid_paths

    def _set_unavilable(self, col, new_array, row):
        #  set row and col as unavailable - keep valid rows and cols for printing
        for i in range(len(new_array)):
            if i != col:
                new_array[row][i] = False
        for i in range(row + 1, len(new_array)):
            new_array[i][col] = False
        #  set diagonal as unavailable - only following rows needed
        for x in range(1, len(new_array)):
            if row + x < len(new_array):
                if col + x < len(new_array):
                    new_array[row + x][col + x] = False
                if col - x >= 0:
                    new_array[row + x][col - x] = False
        return new_array

    def _convert_to_solution_format(self, array):
        output = []
        for r in range(len(array)):
            output.append(''.join(['Q' if c else '.' for c in array[r]]))
        return output


if __name__ == "__main__":
    sol = Solution()
    res = sol.solveNQueens(4)
    print(res)
