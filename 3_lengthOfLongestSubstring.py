from collections import Counter
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0 
        ans = 0
        c = Counter()
        for i, u in enumerate(s):
            c[u] += 1
            while c[u] > 1:
                c[s[left]] -= 1
                left += 1
            right += 1
            ans = max(right-left,ans)
        return ans