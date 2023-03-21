# 52. N-Queens II

class Solution:
    def inner_rec(self, array, row, col):
        if array[row][col] == False:
            return 0
        if row == len(array) - 1:
            return 1
        new_array = [x[:] for x in array]
        #  set row and col as unavailable
        for i in range(len(new_array)):
            new_array[row][i] = False
            new_array[i][col] = False
        #  set diagonal as unavailable
        for x in range(len(new_array)):
            if row + x < len(new_array):
                if col + x < len(new_array):
                    new_array[row + x][col + x] = False
                if col - x >= 0:
                    new_array[row + x][col - x] = False
            if row - x >= 0:
                if col + x < len(new_array):
                    new_array[row - x][col + x] = False
                if col - x >= 0:
                    new_array[row - x][col - x] = False
        # check all col options
        valid_paths = 0
        for col in range(len(new_array)):
            valid_paths += self.inner_rec(new_array, row + 1, col)
        return valid_paths

    def totalNQueens(self, n: int) -> int:
        # create available matrix
        array = [[True for x in range(n)] for y in range(n)]
        valid_paths = 0
        # check all col options
        for col in range(len(array)):
            valid_paths += self.inner_rec(array, 0, col)
        return valid_paths


if __name__ == "__main__":
    sol = Solution()
    res = sol.totalNQueens(5)
    print(res)
