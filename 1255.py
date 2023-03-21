# 1255. Maximum Score Words Formed by Letters
from typing import List
from collections import Counter


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int], points=0) -> int:
        # end recursion
        if len(words) == 0:
            return points

        # current word
        c_letters = letters.copy()
        word = words[0]
        current_points = 0

        valid_word = True
        word_counter = Counter(word)
        input_counter = Counter(c_letters)
        # check word can be used
        for letter, count in word_counter.items():
            if input_counter[letter] < count:
                valid_word = False
        # if word can be used calculate points
        if valid_word:
            for char in word:
                c_letters.remove(char)
                current_points += score[ord(char) - 97]

        # max between using and not using word
        return max(
            self.maxScoreWords(words[1:], letters, score, points),
            self.maxScoreWords(words[1:], c_letters, score, points + current_points),
        )


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.maxScoreWords(
            ["dog", "cat", "dad", "good"],
            ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
            [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    )
