class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Sort the array by the "start" of each interval
        intervals.sort(key = lambda i: i[0])
        output = []
        output.append(intervals[0])

        for start, end in intervals[1:]:

            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        
        return output