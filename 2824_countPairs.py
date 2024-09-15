def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        start = 0
        end = len(nums) - 1
        count = 0
        while start < end:
            if nums[start] + nums[end] < target:
                count += end - start
                start += 1
            else:
                end -= 1
        return count
