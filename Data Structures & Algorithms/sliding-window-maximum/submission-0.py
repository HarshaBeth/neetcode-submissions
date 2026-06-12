class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() # only stores indices of the numbers
        l = r = 0

        while r < len(nums):
            #check if queue is empty
            # pop smaller values from left (always make sure it is in decreasing order)
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # if the left pointer moves ahead and is greater than the index at q[0] (highest), 
            # remove the left most item
            if l > q[0]:
                q.popleft()
        
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        
        return output
            
            

