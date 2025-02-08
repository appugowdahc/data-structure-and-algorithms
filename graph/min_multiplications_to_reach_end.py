from typing import List
from collections import deque
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        if start == end:
            return 0  # If start is already end, no steps are needed

        # Queue for BFS where each entry is (current value, steps taken)
        queue = deque([(start, 0)])
        
        # Visited array to keep track of visited numbers
        visited = [False] * 100000
        visited[start] = True
        
        # BFS loop
        while queue:
            current, steps = queue.popleft()
            
            # Explore each multiplication option
            for num in arr:
                next_val = (current * num) % 100000
                
                # Check if we reached the end
                if next_val == end:
                    return steps + 1
                if next_val > end:
                    return -1
                # If not visited, enqueue the next value
                if not visited[next_val]:
                    visited[next_val] = True
                    queue.append((next_val, steps + 1))
        
        # If end is not reachable
        # print(visited)
        return -1
    
s  = Solution()
print(s.minimumMultiplications([2,4,5],2,9))