def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        idx = {x: i for i, x in enumerate(nums1)}
        st = []
        ans = [-1] * len(nums1)
        for x in reversed(nums2):
            while st and x >= st[-1]:
                st.pop()
            if st and x in idx:
                ans[idx[x]] = st[-1]
            st.append(x)
        return ans