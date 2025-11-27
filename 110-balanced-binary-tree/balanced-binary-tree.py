class Solution:
    def isBalanced(self, root):
        
        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)
            
            # If any subtree is unbalanced, return -1 directly
            if left == -1 or right == -1:
                return -1
            
            # If height difference > 1 → not balanced
            if abs(left - right) > 1:
                return -1
            
            # Otherwise return normal height
            return max(left, right) + 1
        
        # If height() returns -1 → unbalanced
        return height(root) != -1
