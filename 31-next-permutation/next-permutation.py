class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        
        # 1. Find the first index i from the right where nums[i] < nums[i+1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # 2. If such i exists, find j from the right where nums[j] > nums[i]
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        
        # 3. Reverse the portion nums[i+1:]
        left = i + 1
        right = n - 1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
