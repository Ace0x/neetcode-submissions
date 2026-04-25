# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        dum = ListNode()
        dum.next = head
        dum2 = ListNode()
        prev = head
        curr = head
        arr = []
        while curr:
            arr.append(curr)
            curr = curr.next
        curr = head
        l = len(arr) - n
        r = l + 2

        arr = [dum] + arr + [dum2]

        arr[l].next = arr[r]
        print(arr[l].val)
        print(arr[r].val)
        if arr[r] == dum2:
            arr[l].next = None
        

        
        return dum.next
    