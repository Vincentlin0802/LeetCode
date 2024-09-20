from collections import Counter
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        j = 0
        cnt = Counter(nums[:k - 1])
        s = sum(nums[:k - 1])
        for i in range(k-1,len(nums)):
            s += nums[i]
            cnt[nums[i]] += 1
            if len(cnt) == k:
                ans = max(s,ans)
            s -= nums[j]
            cnt[nums[j]] -= 1
            if cnt[nums[j]] == 0:
                del cnt[nums[j]]
            j += 1
        return ans