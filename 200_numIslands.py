class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'  # 标记为已访问
            dfs(grid, i + 1, j)  # 向下
            dfs(grid, i, j + 1)  # 向右
            dfs(grid, i - 1, j)  # 向上
            dfs(grid, i, j - 1)  # 向左
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count