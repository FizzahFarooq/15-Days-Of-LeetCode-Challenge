class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}

        # Build adjacency list
        for a, b in prerequisites:
            graph[b].append(a)

        visited = set()       # nodes fully processed
        visiting = set()      # nodes in current DFS path

        def dfs(course):
            if course in visiting:
                return False      # cycle found
            if course in visited:
                return True       # already checked

            visiting.add(course)

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            visiting.remove(course)
            visited.add(course)
            return True

        # Check all courses
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
