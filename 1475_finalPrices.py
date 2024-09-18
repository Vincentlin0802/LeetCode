def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n = len(prices)
        st = [0]
        ans = [0] * n
        for i in range(n-1,-1,-1):
            p = prices[i]
            while st and p < st[-1]:
                st.pop()
            ans[i] = p - st[-1]
            st.append(p)
        return ans
