# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root,root.val)
    def dfs(self,node, papas):
        if not node:
            return 0
        if papas <= node.val:  
            papas = node.val
            return 1 + self.dfs(node.left,papas) + self.dfs(node.right, papas)
        else:
            return self.dfs(node.left,papas) + self.dfs(node.right,papas)