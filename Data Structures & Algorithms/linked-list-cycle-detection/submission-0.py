# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        Hash = dict()
        curr = head
        

        while curr:
            val = Hash.get(curr)

            if val != None:
                return True
            else:
                Hash[curr] = curr.val
                
                curr = curr.next

        return False
        

