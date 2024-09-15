def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = float('inf')
        least_sum = 0
        for i in range (len(nums) - 2):
            x = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if x+nums[j]+nums[k] > target:
                    if abs(target-(x+nums[j] + nums[k])) < ans:
                        least_sum = x+nums[j] + nums[k]
                        ans = abs(target-(x+nums[j] + nums[k]))
                    k -= 1
                elif x+nums[j]+nums[k] < target:
                    if abs(target-(x+nums[j] + nums[k])) < ans:
                        least_sum = x+nums[j] + nums[k]
                        ans = abs(target-(x+nums[j] + nums[k]))
                    j += 1
                elif x+nums[j] + nums[k] == target:
                    return x+nums[j] + nums[k]
        return least_sum