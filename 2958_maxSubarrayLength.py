from collections import Counter
class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        ans = 0
        c = Counter()
        for right, u in enumerate(nums):
            c[u] += 1
            while c[u] > k:
                c[nums[left]] -= 1
                left += 1
            ans = max(right-left+1,ans)
        return ans