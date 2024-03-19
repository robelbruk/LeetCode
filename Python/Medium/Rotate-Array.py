def rotate(nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import deque
        
        d = deque(nums)
        d.rotate(k)

        for i in range(len(nums)): # 0 - 7
            nums[i] = d[i]