from collections import defaultdict

class Solution:
    def canBeChained(self, arr=["ab" , "bc", "cd", "da"]):
        # Create adjacency list and in-degree/out-degree counts
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        print(f" graph is {graph}")
        print(f"in_degree is {in_degree}")
        print(f"out_Degree is {out_degree}")

        # Build the graph
        for word in arr:
            start, end = word[0], word[-1]
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        # Check if in-degree and out-degree of each character match
        for char in set(in_degree.keys()).union(set(out_degree.keys())):
            if in_degree[char] != out_degree[char]:
                return False

        # Helper function to perform DFS
        def dfs(node, visited, graph):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited, graph)

        # Step 1: Check if all nodes with non-zero degree are connected in original graph
        visited = set()
        first_char = arr[0][0]
        dfs(first_char, visited, graph)
        if any(char not in visited for char in out_degree if out_degree[char] > 0):
            return False

        # Step 2: Transpose the graph
        transposed_graph = defaultdict(list)
        for u in graph:
            for v in graph[u]:
                transposed_graph[v].append(u)

        # Step 3: Check connectivity on the transposed graph
        visited.clear()
        dfs(first_char, visited, transposed_graph)
        if any(char not in visited for char in out_degree if out_degree[char] > 0):
            return False

        # If all checks passed, return True
        return True
s= Solution()
print(s.canBeChained())