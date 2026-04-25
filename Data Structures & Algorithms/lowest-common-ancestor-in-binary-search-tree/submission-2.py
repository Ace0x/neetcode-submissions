# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.l = 0
        self.r = 0
        self.papa = 0
        self.dfs(root)
        
        return self.papa

    def dfs(self,root):
        if self.l:
            return True
        if self.r:
            return True
        if not root:
            return None
        self.l = self.dfs(root.left)
        self.r = self.dfs(root.right)
            
        if root.val >= p.val and root.val <= q.val:
            self.papa = root
            return True
        if root.val <= p.val and root.val >= q.val:
            self.papa = root
            return True
