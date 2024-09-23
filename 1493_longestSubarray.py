class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
    #solution 1 (use hashmap to count)
        """
        left = 0
        ans = 0
        c = Counter()
        for i,u in enumerate(nums):
            c[u] += 1
            while c[0] > 1 :
                c[nums[left]] -= 1
                left += 1
            ans = max(c[1],ans)
        if c[0] == 0:
            ans = len(nums) - 1
        return ans

        """

#solution 2 without hashmap (faster)
        left = 0
        ans = 0
        cnt = 0
        for right, u in enumerate(nums):
            if u == 0:
                cnt += 1
            while cnt > 1:
                if nums[left] == 0:
                    cnt -= 1
                left += 1
            ans = max(right - left,ans)
        return ans 
