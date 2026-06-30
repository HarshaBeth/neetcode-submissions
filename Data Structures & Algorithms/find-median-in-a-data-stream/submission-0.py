class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, num * -1)

        # Now check if all nums in small are <= smallest num in large
        if (self.small and self.large and (self.small[0] * -1) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Now check the lengths of both heaps
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) + 1 < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (self.small[0] * -1 + self.large[0]) / 2


        
        