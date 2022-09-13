import numpy as np
import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        if scoville[0] >= K:
            return count
        
        # Pop minimum two values
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        
        # Calculate blended value
        blended = a + b*2
        
        # Add blended value
        heapq.heappush(scoville, blended)
        
        # Increase count
        count += 1
    if scoville[0] >= K:
            return count    
    else:
        return -1