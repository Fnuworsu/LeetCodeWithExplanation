class Solution:
    class UnionFind:
        def __init__(self, size):
            self.parent = list(range(size))
            self.rank = [1] * size

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])  # Path compression
            return self.parent[x]

        def union(self, x, y):
            rootX = self.find(x)
            rootY = self.find(y)

            if rootX != rootY:
                # Union by rank
                if self.rank[rootX] > self.rank[rootY]:
                    self.parent[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.parent[rootX] = rootY
                else:
                    self.parent[rootY] = rootX
                    self.rank[rootX] += 1

    def countServers(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        uf = self.UnionFind(rows * cols)

        # Helper function to convert 2D grid indices to 1D index
        def to1D(r, c):
            return r * cols + c

        # Union servers in the same row
        for r in range(rows):
            row_servers = []
            for c in range(cols):
                if grid[r][c] == 1:
                    row_servers.append(c)
            for i in range(len(row_servers) - 1):
                uf.union(to1D(r, row_servers[i]), to1D(r, row_servers[i + 1]))

        # Union servers in the same column
        for c in range(cols):
            col_servers = []
            for r in range(rows):
                if grid[r][c] == 1:
                    col_servers.append(r)
            for i in range(len(col_servers) - 1):
                uf.union(to1D(col_servers[i], c), to1D(col_servers[i + 1], c))

        # Count the number of servers that communicate with at least one other server
        server_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # A server communicates if it is in a set with more than one element
                    if uf.find(to1D(r, c)) != to1D(r, c):
                        server_count += 1
                    else:
                        # Check if any other server is in the same set (row or column)
                        connected = False
                        for i in range(cols):
                            if i != c and grid[r][i] == 1 and uf.find(to1D(r, c)) == uf.find(to1D(r, i)):
                                connected = True
                                break
                        if not connected:
                            for i in range(rows):
                                if i != r and grid[i][c] == 1 and uf.find(to1D(r, c)) == uf.find(to1D(i, c)):
                                    connected = True
                                    break
                        if connected:
                            server_count += 1

        return server_count
