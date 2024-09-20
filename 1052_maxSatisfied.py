class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        s = [0,0]
        max_s1 = 0
        arr = zip(customers,grumpy)
        for i,(c,g) in enumerate(arr):
            s[g] += c
            if i < minutes - 1:
                continue
            max_s1 = (max_s1,s[1])
            if grumpy[i - minutes + 1]:
                s[1] -= customers[i - minutes + 1]  #如果窗口的左边界是情绪不稳定，减去其影响
        return s[0] + max_s1
