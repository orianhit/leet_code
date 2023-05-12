# 895. Maximum Frequency Stack
#  Litals

from collections import defaultdict, Counter


class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.counts_dict = defaultdict(list)
        self.counter = Counter()

    def push(self, val: int) -> None:
        self.counter[val] += 1
        # each new val is simply new occurrence of the value
        # but still in the count - i counts (if count is 3 should be in 1+2+3)
        self.counts_dict[self.counter[val]].append(val)

        # update max_freq if current counter is bigger
        self.max_freq = max(self.max_freq, self.counter[val])

    def pop(self) -> int:
        output = self.counts_dict[self.max_freq].pop()
        self.counter[output] -= 1

        # if no more numbers for this max frequency decrease max_freq by 1 (always exists)
        if not self.counts_dict[self.max_freq]:
            self.max_freq -= 1
        return output



if __name__ == "__main__":
    obj = FreqStack()
    for val in [5, 7, 5, 7, 4, 5]:
        obj.push(val)
    for i in range(4):
        param_2 = obj.pop()
        print(param_2)