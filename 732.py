# 732. My Calendar III
from collections import defaultdict


def append_if_diff(arr, item):
    if item[0] != item[1]:
        arr.append(item)


class MyCalendarThree:

    def __init__(self):
        self.max_common_spans = list()
        pass

    def book(self, startTime: int, endTime: int) -> int:
        updated_key = False

        new_common_spans = []
        for start_span, end_span, weight in self.max_common_spans:
            if startTime > end_span:
                append_if_diff(new_common_spans, (start_span, end_span, weight))
            elif startTime == start_span:
                if endTime == end_span:
                    append_if_diff(new_common_spans, (startTime, endTime, weight + 1))
                    updated_key = True
                elif endTime < end_span:
                    append_if_diff(new_common_spans, (startTime, endTime, weight + 1))
                    append_if_diff(new_common_spans, (endTime, end_span, weight))
                    updated_key = True
                else: # endTime > end_span
                    append_if_diff(new_common_spans, (start_span, end_span, weight + 1))
                    startTime = end_span
            elif startTime < start_span:
                if endTime <= start_span:
                    if not updated_key:
                        append_if_diff(new_common_spans, (startTime, endTime, 1))
                    append_if_diff(new_common_spans, (start_span, end_span, weight))
                    if updated_key:
                        continue
                elif endTime == end_span:
                    append_if_diff(new_common_spans, (startTime, start_span, 1))
                    append_if_diff(new_common_spans, (start_span, end_span, weight + 1))
                elif endTime < end_span:
                    append_if_diff(new_common_spans, (startTime, start_span, 1))
                    append_if_diff(new_common_spans, (start_span, endTime, weight + 1))
                    append_if_diff(new_common_spans, (endTime, end_span, weight))
                else: # endTime > end_span
                    append_if_diff(new_common_spans, (startTime, start_span, 1))
                    append_if_diff(new_common_spans, (start_span, end_span, weight + 1))
                    startTime = end_span
                updated_key = True
            else:  # start_span < startTime < end_span
                append_if_diff(new_common_spans, (start_span, startTime, weight))
                if endTime == end_span:
                    append_if_diff(new_common_spans, (startTime, end_span, weight + 1))
                    updated_key = True
                elif endTime < end_span:
                    append_if_diff(new_common_spans, (start_span, endTime, weight + 1))
                    append_if_diff(new_common_spans, (endTime, end_span, weight))
                    updated_key = True
                else: # endTime > end_span
                    append_if_diff(new_common_spans, (startTime, end_span, weight + 1))
                    startTime = end_span

        if not updated_key: # aka bigger then all nodes
            append_if_diff(new_common_spans, (startTime, endTime, 1))
        self.max_common_spans = new_common_spans

        return max(self.max_common_spans, key=lambda x: x[2])[2]


if __name__ == "__main__":
    sol = MyCalendarThree()
    idx = 0
    for book in [[],[12,26],[37,47],[90,100],[21,34],[99,100],[95,100],[4,16],[67,86],[55,69],[63,81],[51,66],[18,35],[51,64],[40,56],[11,28],[13,27],[38,51],[71,89],[12,27],[35,50],[92,100],[48,59],[81,92],[96,100],[98,100],[63,74],[41,51],[61,76],[27,39],[70,84],[56,75],[21,31],[63,79],[31,43],[26,44],[25,43],[42,58],[30,43],[19,31],[26,37],[94,100],[55,69],[7,20],[96,100],[91,100],[76,87],[59,75],[9,24],[22,32],[3,21],[72,88],[29,43],[74,84],[1,19],[14,33],[62,79],[47,57],[96,100],[67,84],[53,66]]:
        if len(book) == 0:
            print('null')
        else:
            res = sol.book(*book)
            print(res)
        idx += 1
