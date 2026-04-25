# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.visited = []
        self.dfs(root,k)
        return self.visited[k-1]
    def dfs(self, node, k):
        if node:
            self.dfs(node.left,k) 
            print()
            self.visited.append(node.val)
            self.dfs(node.right,k)
        if len(self.visited) == k:
            return self.visited[k-1]
        return  0