class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

# Create object and call method
sol = Solution()
param_1 = "anagram"
param_2 = "nagaram"
ret = sol.isAnagram(param_1, param_2)
print(ret)  # True
