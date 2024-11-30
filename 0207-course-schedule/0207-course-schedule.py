class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def canComplete(course, visited, currPath, graph):
            if course in visited:
                return True
            if course in currPath:
                return False
            
            currPath.add(course)
            for preq in graph[course]:
                if not canComplete(preq, visited, currPath, graph):
                    return False

            visited.add(course)
            currPath.remove(course)

            return True

        graph = defaultdict(list)
        for course, preq in prerequisites:
            graph[course].append(preq)

        visited = set()
        currPath = set()

        for i in range(numCourses):
            if i not in visited and not canComplete(i, visited, currPath, graph):
                return False

        return True                             
        