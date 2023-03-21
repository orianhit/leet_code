# 2136. Earliest Possible Day of Full Bloom

class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """
        sorted_by_grow = [i for i,_ in sorted(enumerate(growTime), key=lambda x: -x[1])]
        overall_grow = 0
        overall = 0

        for idx in range(len(plantTime)):
            overall_grow += plantTime[sorted_by_grow[idx]]
            overall = max(overall_grow + growTime[sorted_by_grow[idx]], overall)

        return overall



if __name__ == "__main__":
    sol = Solution()
    print(sol.earliestFullBloom([27,5,24,17,27,4,23,16,6,26,13,17,21,3,9,10,28,26,4,10,28,2], [26,9,14,17,6,14,23,24,11,6,27,14,13,1,15,5,12,15,23,27,28,12]))
