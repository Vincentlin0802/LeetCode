def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0 
        for i in range(2,len(nums)):
            a = nums[i]
            j = 0
            k =  i - 1
            while j < k:
                if nums[j] + nums[k] > a:
                    count += k-j
                    k -= 1
                else:
                    j+=1
        return count