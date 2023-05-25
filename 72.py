# 72. Edit Distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        first_word_size = len(word1) + 1
        sec_word_size = len(word2) + 1
        dynamic_cache = [[0] * (sec_word_size) for _ in range(first_word_size)]

        for i in range(first_word_size):
            for j in range(sec_word_size):
                if i == 0:  # second word vs empty string
                    dynamic_cache[0][j] = j
                elif j == 0:  # first word vs empty string
                    dynamic_cache[i][0] = i
                elif word1[i - 1] == word2[j - 1]:  # if current letter is the same
                    dynamic_cache[i][j] = dynamic_cache[i - 1][j - 1]  # should be the diagonal (aka without the word)
                else:
                    diagonal_val = dynamic_cache[i - 1][j - 1]
                    without_first_word_last_letter = dynamic_cache[i - 1][j]
                    without_second_word_last_letter = dynamic_cache[i][j - 1]
                    dynamic_cache[i][j] = min(diagonal_val,
                                              without_first_word_last_letter,
                                              without_second_word_last_letter) + 1  # plus one change

        return dynamic_cache[first_word_size - 1][sec_word_size - 1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minDistance("horse", "ros"))
