class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, preq in prerequisites:
            graph[course].append(preq)

        visited, visiting = set(), set()

        def dfs(course, graph):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)

            for preq in graph[course]:
                if not dfs(preq,graph):
                    return False

            visited.add(course)
            visiting.remove(course)

            return True

        for node in range(numCourses):
            if not dfs(node, graph):
                return False

        return True                    
