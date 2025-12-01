class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]     # base index
        longest = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()

                # if stack becomes empty, push current index
                if not stack:
                    stack.append(i)
                else:
                    longest = max(longest, i - stack[-1])

        return longest
