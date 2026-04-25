"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        h = defaultdict(None)
        dumb = Node(0)
        ned = dumb
        while curr:
            h[curr] = Node(x = curr.val)
            curr = curr.next
        curr = head
        if curr:
            dumb.next = h[curr]
            if curr.random:
                dumb.next.random = h[curr.random]
            if curr.next:
                dumb.next.next = h[curr.next]
            curr = curr.next
        while curr:
            node = h[curr]
            if curr.next:
                node.next = h[curr.next]
            if curr.random: 
                node.random = h[curr.random]
            curr = curr.next
        return dumb.next
