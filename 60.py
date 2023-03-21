# 60. Permutation Sequence
#todo: send

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        access = k - 1 # index starts with 0, aka 1 means no permutations available
        available_numbers = [i + 1 for i in range(n)]
        out_string = ''
        factorial_cache = [1] * (n-1)
        for i in range(1, n - 1):
            factorial_cache[i] = factorial_cache[i - 1] * (i + 1)

        for i in range(n):
            factorial_of_sub_number = factorial_cache[n - 1 - i - 1]  # minus 1 for 0index, and another for one letter less
            sub_number_permutations = access // factorial_of_sub_number
            access = access % factorial_of_sub_number
            out_string += str(available_numbers[sub_number_permutations])
            available_numbers.pop(sub_number_permutations)

        return out_string




if __name__ == "__main__":
    sol = Solution()
    print(sol.getPermutation(4, 9))