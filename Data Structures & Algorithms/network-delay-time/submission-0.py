class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, t in times:
            edges[u].append((v, t))
        
        minHeap = [(0, k)]
        visit = set()
        time = 0

        while minHeap:
            time1, node1 = heapq.heappop(minHeap)

            if node1 in visit:
                continue
            
            visit.add(node1)
            time = max(time, time1)

            for node2, time2 in edges[node1]:
                if node2 not in visit:
                    heapq.heappush(minHeap, (time1 + time2, node2))
        
        return time if len(visit) == n else -1