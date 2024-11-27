def pondSizes(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[int]
        """
        m,n = len(land),len(land[0])
        def dfs(i,j):
            if 0 <= i< m and  0 <= j< n and land[i][j] == 0 :
                land[i][j] = 1
                return 1+ dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)+dfs(i+1,j+1)+dfs(i-1,j-1)+dfs(i+1,j-1)+dfs(i-1,j+1)
            return 0 
        
        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0:
                    res.append(dfs(i,j))
        res.sort()
        return res