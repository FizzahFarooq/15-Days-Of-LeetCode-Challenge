class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prevHeight):
            if (r, c) in visited:
                return
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if heights[r][c] < prevHeight:
                return

            visited.add((r, c))

            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        # Start DFS from the edges touching Pacific Ocean
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])       # top edge
            dfs(rows-1, c, atlantic, heights[rows-1][c]) # bottom edge

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])       # left edge
            dfs(r, cols-1, atlantic, heights[r][cols-1]) # right edge

        result = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result
