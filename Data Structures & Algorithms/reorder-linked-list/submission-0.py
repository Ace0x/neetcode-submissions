# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return
        
        # 1. Put all nodes into an array
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        
        # 2. Use two pointers to re-link
        left, right = 0, len(arr) - 1
        
        while left < right:
            # Link Left -> Right
            arr[left].next = arr[right]
            left += 1
            
            # If pointers met, stop here to avoid self-cycle
            if left == right: 
                break
                
            # Link Right -> Next Left
            arr[right].next = arr[left]
            right -= 1
        
        # 3. CRITICAL STEP: Terminate the list!
        # The last node processed (arr[left]) likely still points to 
        # its old neighbor. We must set it to None to prevent a cycle.
        arr[left].next = None