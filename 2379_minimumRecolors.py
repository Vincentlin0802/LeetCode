class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        ans = float('inf')
        cnt = 0
        for i,u in enumerate(blocks):
            if u == "W":
                cnt +=1
            if i >= k and blocks[i-k] == "W":
                cnt -=1     
            if i >= k -1 :
                ans = min(ans,cnt)
        return ans

                

                
