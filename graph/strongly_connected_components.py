from collections import defaultdict
class Solution:
    def kosaraju(self, V=5, adj={0:[2,3],1:[0],2:[1],3:[4],4:[]}):
        # Step 1: DFS to fill the stack according to finishing time
        def dfs1(v, visited, stack):
            visited[v] = True
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    dfs1(neighbor, visited, stack)
            stack.append(v)

        # Step 2: Transpose the graph
        def transpose_graph():
            transposed_adj = [[] for _ in range(V)]
            for i in range(V):
                for neighbor in adj[i]:
                    transposed_adj[neighbor].append(i)
            return transposed_adj

        # Step 3: DFS on transposed graph to find SCCs
        def dfs2(v, visited, transposed_adj):
            visited[v] = True
            for neighbor in transposed_adj[v]:
                if not visited[neighbor]:
                    dfs2(neighbor, visited, transposed_adj)

        # Step 1: Fill vertices in stack according to their finishing times
        stack = []
        visited = [False] * V
        for i in range(V):
            print("HI")
            if not visited[i]:
                dfs1(i, visited, stack)
            if not False in visited:
                break
        # Step 2: Create the transposed graph
        transposed_adj = transpose_graph()

        # Step 3: Process all vertices in order defined by the stack
        visited = [False] * V
        scc_count = 0
        while stack:
            node = stack.pop()
            if not visited[node]:
                # Each DFS call here represents a new SCC
                dfs2(node, visited, transposed_adj)
                scc_count += 1
        
        return scc_count
s = Solution()
print(s.kosaraju())
d = defaultdict()
CX