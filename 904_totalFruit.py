from collections import Counter
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left = 0
        ans = 0
        c = Counter()
        for right,u in enumerate(fruits):
            c[u] += 1
            while len(c) > 2:
                c[fruits[left]] -= 1
                if c[fruits[left]] == 0:
                    del(c[fruits[left]])
                left += 1
            ans = max(right-left + 1,ans)
        return ans