class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        """
        0 = not visited, 1 = visited, 2 = done 
        """
        state = [0 for _ in range(numCourses)] 

        for course, preq in prerequisites:
            graph[course].append(preq)

        def completeCourse(course, graph):
            if state[course] == 1:
                return False

            if state[course] == 2:
                return True

            state[course] = 1

            for preq in graph[course]:
                if not completeCourse(preq, graph):
                    return False

            state[course] = 2
            return True   

        for course in range(numCourses):
            if not completeCourse(course, graph):
                return False

        return True                         
                
        