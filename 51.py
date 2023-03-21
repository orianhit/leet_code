# 51. N-Queens
from typing import List


class Solution:

    def array_to_solution(self, array):
        output = []
        for r in range(len(array)):
            output.append(''.join(['Q' if c else '.' for c in array[r]]))
        return output

    def inner_rec(self, array, row, col):
        if not array[row][col]:
            return False
        if row == len(array) - 1:
            return [self.array_to_solution(array)]

        new_array = [x[:] for x in array]
        #  set row and col as unavailable
        for i in range(len(new_array)):
            if i != col:
                new_array[row][i] = False
        for i in range(row + 1, len(new_array)):
            new_array[i][col] = False

        #  set diagonal as unavailable
        for x in range(1, len(new_array)):
            if row + x < len(new_array):
                if col + x < len(new_array):
                    new_array[row + x][col + x] = False
                if col - x >= 0:
                    new_array[row + x][col - x] = False
        # check all col options
        valid_paths = []
        for col in range(len(new_array)):
            inner_array = self.inner_rec(new_array, row + 1, col)
            if inner_array:
                valid_paths += inner_array
        return valid_paths

    def solveNQueens(self, n: int) -> List[List[str]]:
        # create available matrix
        array = [[True for x in range(n)] for y in range(n)]
        valid_paths = []
        # check all col options
        for col in range(len(array)):
            inner_array = self.inner_rec(array, 0, col)
            if inner_array:
                valid_paths += inner_array
        return valid_paths


if __name__ == "__main__":
    sol = Solution()
    res = sol.solveNQueens(4)
    print(res)
