class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        windowSize = n - k
        min_s = s = sum(cardPoints[:windowSize])
        for i in range(windowSize,n):
            s += cardPoints[i] - cardPoints[i-windowSize]
            min_s = min(s,min_s)
        return sum(cardPoints) - min_s