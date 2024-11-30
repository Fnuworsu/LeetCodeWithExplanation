class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        graph = defaultdict(list)

        for course, preq in prerequisites:
            graph[course].append(preq)    
        
        def canComplete(course, graph):
            #cycle detection
            if course in visited:
                return False

            if graph[course] == []:
                return True

            visited.add(course)

            for preq in graph[course]:
                if not canComplete(preq, graph):
                    return False

            #done with that course
            visited.remove(course)
            #mark as completed
            graph[course] = []  

            return True                  
        
        for course in range(numCourses):
            if not canComplete(course, graph):
                return False

        return True        