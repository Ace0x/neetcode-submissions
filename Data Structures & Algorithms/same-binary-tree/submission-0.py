# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.l = list()
        self.r = list()

        self.dfs(p,self.l)
        self.dfs(q,self.r)
        if self.l != self.r:
            return False
        return True
    def dfs(self,root,s):
        if not root:
            s.append(None)
            return None
        self.dfs(root.left,s)
        self.dfs(root.right,s)

        s.append(root.val)
        