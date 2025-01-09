class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for course, preq in prerequisites:
            graph[course].append(preq)

        state = [0 for _ in range(numCourses)]    

        def complete(course):
            #return bool if we acn complete course or not
            if state[course] == 2:
                return True
            if state[course] == 1:
                return False

            state[course] = 1

            for nb in graph[course]:
                if not complete(nb):
                    return False

            state[course] = 2
            return True   

        for course in range(numCourses):
            if not complete(course):
                return False

        return True                   
        