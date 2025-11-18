class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        if n == 0:
            return []
        answer = [1] * n

        # prefix products
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        # suffix products multiplied into answer
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer
