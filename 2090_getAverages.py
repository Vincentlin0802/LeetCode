class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = [-1] * n
        if k * 2 + 1 <= n:
            total = sum(nums[:k * 2 + 1])
            for i in range(k,n-k):
                if i != k:
                    total += nums[i + k] - nums[i - k - 1]
                ans[i] = total // ((2*k)+1)
        return ans
