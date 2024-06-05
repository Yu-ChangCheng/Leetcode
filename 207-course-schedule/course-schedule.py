class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        seen = set()
        lookup = defaultdict(list)

        for course, pre in prerequisites:
            lookup[course].append(pre)
        
        def dfs(course):
            if course in seen:
                return False
            if lookup[course] == []:
                return True
            seen.add(course)
            for pre in lookup[course]:
                if dfs(pre) == False:
                    return False
            seen.remove(course)
            lookup[course] = []
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True


        seen = set()
        lookup = defaultdict(list)

        for course, pre in prerequisites:
            lookup[course].append(pre)
        
        def dfs(course):
            if course in seen:
                return False
            if lookup[course] == []:
                return True
            seen.add(course)
            for pre in lookup[course]:
                if not dfs(pre):
                    return False
            seen.remove(course)
            lookup[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True