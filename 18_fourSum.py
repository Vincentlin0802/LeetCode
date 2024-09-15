def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = []
        for a in range(n-3):
            x = nums[a]
            if a and x == nums[a-1]:
                continue
            if x + nums[a+1] + nums[a+2] + nums[a+3] > target: #优化1
                break
            if x + nums[n-1] + nums[n-2] + nums[n-3] <  target: #优化2 
                continue
            for b in range (a+1, n-2):
                y = nums[b]
                if b > a+1 and y == nums[b-1]:
                    continue
                if x + y + nums[b+1] + nums[b+2] > target:  #优化1
                    break
                if x + y + nums[n-1] + nums[n-2] < target:  #优化2
                    continue
                c = b + 1
                d = n - 1
                while c<d:
                    if x + y + nums[c] + nums[d] > target:
                        d -= 1
                    elif x + y + nums[c] + nums[d] < target:
                        c += 1
                    else:
                        ans.append([x,y,nums[c],nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c - 1]:  # 跳过重复数字
                            c += 1
                        d -= 1
                        while d > c and nums[d] == nums[d + 1]:  # 跳过重复数字
                            d -= 1
        return ans