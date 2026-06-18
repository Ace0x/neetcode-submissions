# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        prev = None
        cur = head

        while cur.next != None:
            print(cur.val)
            prev = cur
            cur = cur.next
            mx = 1
            
            for i in range(1,max(cur.val,prev.val)+1):
                if cur.val % i == 0 and prev.val % i == 0:
                    mx = i
            tmp = ListNode(mx)
            prev.next = tmp
            tmp.next = cur

        return head
        

