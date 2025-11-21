class Solution:
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                # return 1-indexed indices per problem
                return [i + 1, j + 1]
            elif s < target:
                i += 1
            else:
                j -= 1
        return []
