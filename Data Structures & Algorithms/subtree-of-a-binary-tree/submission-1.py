# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not (p or q):
                return True
            elif (p and not q) or (q and not p):
                return False
            elif p.val != q.val:
                return False
            else:
                left = isSameTree(p.left, q.left)
                right = isSameTree(p.right, q.right)
                return left and right
        if not (root or subRoot):
            return True
        elif (root and not subRoot) or (subRoot and not root):
            return False
        else:
            if isSameTree(root, subRoot):
                return True
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            return left or right


