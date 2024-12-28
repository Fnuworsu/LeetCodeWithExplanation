class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        state = [0 for _ in range(numCourses)]
        res = []

        for u,v in prerequisites:
            graph[u].append(v)

        def dfs(course):
            nonlocal res
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True

            state[course] = 1

            for preq in graph[course]:
                if not dfs(preq):
                    return False

            state[course] = 2
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res                        
                