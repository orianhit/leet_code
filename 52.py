# 52. N-Queens II

class Solution:
    def totalNQueens(self, n: int) -> int:
        # create available matrix
        array = [[True for x in range(n)] for y in range(n)]
        valid_paths = 0
        # check all col options
        for col in range(len(array)):
            valid_paths += self._inner_rec(array, 0, col)
        return valid_paths

    def _inner_rec(self, array, row, col):
        if array[row][col] == False: # return failure if blocked
            return 0
        if row == len(array) - 1:  # return success if done all columns
            return 1
        new_array = [x[:] for x in array]  # duplicate_array
        new_array = self._set_unavailables(col, new_array, row)
        # check all col options
        valid_paths = 0
        for col in range(len(new_array)):
            valid_paths += self._inner_rec(new_array, row + 1, col)
        return valid_paths

    def _set_unavailables(self, col, new_array, row):
        # set row and col as unavailable - no need to preserve old rows & cols
        for i in range(len(new_array)):
            new_array[row][i] = False
            new_array[i][col] = False
        #  set diagonal as unavailable - only following rows needed
        for x in range(len(new_array)):
            if row + x < len(new_array):
                if col + x < len(new_array):
                    new_array[row + x][col + x] = False
                if col - x >= 0:
                    new_array[row + x][col - x] = False
        return new_array


if __name__ == "__main__":
    sol = Solution()
    res = sol.totalNQueens(5)
    print(res)
