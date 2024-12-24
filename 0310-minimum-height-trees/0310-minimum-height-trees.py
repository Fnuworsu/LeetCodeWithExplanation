from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Base case for a single node
        if n == 1:
            return [0]  # The single node is the root
        
        # Build the graph as an adjacency list
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Find all initial leaves (nodes with one connection)
        leaves = deque([node for node in range(n) if len(graph[node]) == 1])

        # Remaining nodes to process
        remaining_nodes = n
        while remaining_nodes > 2:
            leaf_count = len(leaves)
            remaining_nodes -= leaf_count
            for _ in range(leaf_count):
                leaf = leaves.popleft()
                # Remove the leaf from its neighbor
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                    # If the neighbor becomes a leaf, add it to the queue
                    if len(graph[neighbor]) == 1:
                        leaves.append(neighbor)
                # Remove the leaf node from the graph
                del graph[leaf]

        # The remaining nodes are the roots of the Minimum Height Trees
        return list(leaves)
