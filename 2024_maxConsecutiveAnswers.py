from collections import Counter
class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        left = 0
        ans = 0
        c = Counter()
        for right, u in enumerate(answerKey):
            c[u] += 1
            while c["T"] > k and c["F"] > k:
                c[answerKey[left]] -= 1
                left += 1
            ans = max(right-left+1,ans)
        return ans
