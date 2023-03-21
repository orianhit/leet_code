# 732. My Calendar III

def append_if_diff(arr, item):
    if item[0] != item[1]:  # if start different from end span time
        arr.append(item)


class MyCalendarThree:

    def __init__(self):
        self.max_common_spans = list()

    def book(self, startTime: int, endTime: int) -> int:
        already_added_span = False

        new_common_spans = []
        for start_span, end_span, weight in self.max_common_spans:
            #  each time new book is added we check which time span it is in
            if startTime > end_span:  # if it started after current span
                append_if_diff(new_common_spans, (start_span, end_span, weight))

            elif startTime == start_span:
                # %->%
                # %->%
                if endTime == end_span:
                    append_if_diff(new_common_spans, (startTime, endTime, weight + 1))
                    already_added_span = True  # mark as already added span
                # %->%
                # %->->%
                elif endTime < end_span:
                    append_if_diff(new_common_spans, (startTime, endTime, weight + 1))
                    append_if_diff(new_common_spans, (endTime, end_span, weight))
                    already_added_span = True
                # %->->%
                # %->%
                else:  # endTime > end_span
                    append_if_diff(new_common_spans, (start_span, end_span, weight + 1))
                    startTime = end_span  # trailing span

            elif startTime < start_span:
                # %->%
                # ->->->%
                if endTime <= start_span:
                    if not already_added_span:  # before all spans
                        append_if_diff(new_common_spans, (startTime, endTime, 1))
                    append_if_diff(new_common_spans, (start_span, end_span, weight))
                # %->->->->%
                # ->->->%->%
                elif endTime == end_span:
                    append_if_diff(new_common_spans, (startTime, start_span, 1))
                    append_if_diff(new_common_spans, (start_span, end_span, weight + 1))
                # %->->->->%
                # ->->->%->->%
                elif endTime < end_span:
                    append_if_diff(new_common_spans, (startTime, start_span, 1))
                    append_if_diff(new_common_spans, (start_span, endTime, weight + 1))
                    append_if_diff(new_common_spans, (endTime, end_span, weight))
                # %->->->->->%
                # ->->->%->%
                else:  # endTime > end_span
                    append_if_diff(new_common_spans, (startTime, start_span, 1))
                    append_if_diff(new_common_spans, (start_span, end_span, weight + 1))
                    startTime = end_span  # trailing span
                already_added_span = True

            # ->%
            # %->->%
            else:  # start_span < startTime < end_span
                append_if_diff(new_common_spans, (start_span, startTime, weight))
                # ->%->%
                # %->->%
                if endTime == end_span:
                    append_if_diff(new_common_spans, (startTime, end_span, weight + 1))
                    already_added_span = True
                # ->%->%
                # %->->->%
                elif endTime < end_span:
                    # append_if_diff(new_common_spans, (start_span, endTime, weight + 1))
                    append_if_diff(new_common_spans, (startTime, endTime, weight + 1))
                    append_if_diff(new_common_spans, (endTime, end_span, weight))
                    already_added_span = True
                # ->%->->%
                # %->->%
                else:  # endTime > end_span
                    append_if_diff(new_common_spans, (startTime, end_span, weight + 1))
                    startTime = end_span

        if not already_added_span:  # aka end after all spans
            append_if_diff(new_common_spans, (startTime, endTime, 1))
        self.max_common_spans = new_common_spans

        return max(self.max_common_spans, key=lambda x: x[2])[2]  # 2 aka weight -> argmax


if __name__ == "__main__":
    sol = MyCalendarThree()
    idx = 0
    for book in [[], [12, 26], [37, 47], [90, 100], [21, 34], [99, 100], [95, 100], [4, 16], [67, 86], [55, 69],
                 [63, 81], [51, 66], [18, 35], [51, 64], [40, 56], [11, 28], [13, 27], [38, 51], [71, 89], [12, 27],
                 [35, 50], [92, 100], [48, 59], [81, 92], [96, 100], [98, 100], [63, 74], [41, 51], [61, 76], [27, 39],
                 [70, 84], [56, 75], [21, 31], [63, 79], [31, 43], [26, 44], [25, 43], [42, 58], [30, 43], [19, 31],
                 [26, 37], [94, 100], [55, 69], [7, 20], [96, 100], [91, 100], [76, 87], [59, 75], [9, 24], [22, 32],
                 [3, 21], [72, 88], [29, 43], [74, 84], [1, 19], [14, 33], [62, 79], [47, 57], [96, 100], [67, 84],
                 [53, 66]]:
        if len(book) == 0:
            print('null')
        else:
            res = sol.book(*book)
            print(res)
        idx += 1
