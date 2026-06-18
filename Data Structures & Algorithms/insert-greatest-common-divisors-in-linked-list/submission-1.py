# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        prev = None
        cur = head
        def mcd(a,b):
            while b > 0:
                a, b = b, a % b
            return a
        while cur.next != None:
            print(cur.val)
            prev = cur
            cur = cur.next
            mx = 1
            
            mx = mcd(prev.val,cur.val)
            
            tmp = ListNode(mx)
            prev.next = tmp
            tmp.next = cur

        return head
        

