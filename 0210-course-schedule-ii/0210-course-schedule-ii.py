class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        state = [0 for _ in range(numCourses)]
        res = []

        for course, preq in prerequisites:
            graph[course].append(preq)

        def complete(course, graph):
            nonlocal res
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True

            state[course] = 1

            for preq in graph[course]:
                if not complete(preq, graph):
                    return False

            res.append(course)
            state[course] = 2
            return True                
            

        for course in range(numCourses):
            if not complete(course, graph):
                return []

        return res            

        