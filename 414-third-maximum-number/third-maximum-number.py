class Solution:
    def thirdMax(self, nums):
        first = second = third = None

        for n in nums:
            if n == first or n == second or n == third:
                continue

            if first is None or n > first:
                first, second, third = n, first, second
            elif second is None or n > second:
                second, third = n, second
            elif third is None or n > third:
                third = n

        return third if third is not None else first
