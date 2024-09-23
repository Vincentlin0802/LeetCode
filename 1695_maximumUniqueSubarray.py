from collections import Counter
class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        ans = 0
        c = Counter()
        for right,u in enumerate(nums):
            c[u] += 1
            while c[u] > 1:
                c[nums[left]] -= 1
                left += 1
            ans = max(sum(nums[left:right+1]),ans)
        return ans