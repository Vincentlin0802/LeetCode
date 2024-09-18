def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        st = []
        for i,h in enumerate(height):
            while st and h >= height[st[-1]]:
                bottom_h = height[st.pop()]
                if len(st) == 0:
                    break
                left = st[-1]
                dh =  min(height[left],h) - bottom_h
                ans += dh * (i-left-1)
            st.append(i)
        return ans