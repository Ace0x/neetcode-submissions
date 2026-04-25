# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.bfs(root)
    def bfs(self,root):
        q = deque([root])
        a = []
        i = 1
        while q:
            level = []
            s = len(q)
            for i in range(s):
                n = q.popleft()
                if n:
                    level.append(n.val)
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
            if len(level) > 0:
                a.append(level)
        return a

        