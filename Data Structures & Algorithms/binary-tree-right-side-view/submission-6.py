# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.dfs(root,0)
        return self.result
    def dfs(self,node, depth):
        if not node:
            return
        if depth == len(self.result):      # first time we reach this depth
            self.result.append(node.val)
        self.dfs(node.right, depth + 1) # go right first
        self.dfs(node.left, depth + 1)

        