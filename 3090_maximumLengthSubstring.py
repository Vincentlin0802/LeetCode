from collections import Counter
class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        ans = 0
        c = Counter()
        for right, u in enumerate(s):
            c[u] += 1
            while c[u] > 2:
                c[s[left]] -= 1
                left += 1
            ans = max(right - left + 1,ans)
        return ans