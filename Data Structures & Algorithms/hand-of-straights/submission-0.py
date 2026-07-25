class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        # This is to keep count of the numbers available
        count = {}
        for i in range(len(hand)):
            count[hand[i]] = 1 + count.get(hand[i], 0)
        
        minHeap = list(count.keys())
        heapq.heapify(minHeap) # O(n)

        while minHeap:
            begin = minHeap[0]

            # Check every "bucket"
            for i in range(begin, begin+groupSize):
                if i not in count: # If the number we're looking for isn't available
                    return False
                
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        
        return True
