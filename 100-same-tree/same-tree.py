class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        # If both are None → trees are same
        if not p and not q:
            return True
        
        # If one is None or values don't match → not same
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check left and right side
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
