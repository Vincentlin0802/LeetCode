class Solution(object):
    def maxSum(self, nums, m, k):
        """
        :type nums: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        ans = 0
        j = 0
        s = sum(nums[:k-1])
        cnt = Counter(nums[:k-1]) 
        for i in range(k-1,len(nums)):
            cnt[nums[i]] += 1
            s += nums[i]
            if len(cnt) >= m:
                ans = max(ans,s)
            cnt[nums[j]] -= 1
            if cnt[nums[j]] == 0:
                del cnt[nums[j]]
            s -= nums[j]
            j += 1
        return ans