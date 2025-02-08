from collections import deque,defaultdict
class Solution:
    def findOrder(self, n, m, prerequisites):
        adj_list = defaultdict(list)
        in_degree = [0] * n
        
        # Step 2: Build the graph
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            in_degree[dest] += 1
    
        # Step 3: Initialize queue with tasks having in-degree 0
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        ordering = []
    
        # Step 4: Process each task
        while queue:
            task = queue.popleft()
            ordering.append(task)
            
            for neighbor in adj_list[task]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
    
        # If ordering contains all tasks, return it. Otherwise, return empty array.
        return ordering if len(ordering) == n else []

################################## 

def findOrder(n, prerequisites):
    # Step 1: Build the graph
    adj_list = defaultdict(list)
    for dest, src in prerequisites:
        adj_list[src].append(dest)
    
    # Step 2: Initialize visited array and result list
    visited = [0] * n
    ordering = []
    
    # Step 3: Define DFS function
    def dfs(task):
        if visited[task] == 1:   # Cycle detected
            return False
        if visited[task] == 2:   # Already processed
            return True

        visited[task] = 1        # Mark as visiting

        # Visit all dependent tasks
        for neighbor in adj_list[task]:
            if not dfs(neighbor):
                return False
        
        visited[task] = 2        # Mark as visited
        ordering.append(task)     # Add to result in reverse order of completion
        return True

    # Step 4: Run DFS for each task
    for task in range(n):
        if visited[task] == 0:
            if not dfs(task):
                return []  # Return empty list if a cycle is detected

    # Step 5: Reverse ordering to get the correct topological order
    return ordering[::-1]

# Example usage
n = 4
prerequisites = [[1, 0], [2, 1], [3, 2]]
result = findOrder(n, prerequisites)
print(result if result else "No Ordering Possible")
