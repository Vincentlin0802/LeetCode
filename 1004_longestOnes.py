def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = ans = cnt0 =0
        for right, x in enumerate(nums):
            cnt0 += 1 - x
            while cnt0 > k:
                cnt0 -= 1 - nums[left]
                left += 1
            ans = max(right - left + 1,ans)
        return ans