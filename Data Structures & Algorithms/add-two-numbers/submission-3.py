# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        dumb = res
        rem = 0
        up = l1
        down = l2
        while up and down:
            node = ListNode()
            res.next = node
            s = up.val + down.val + rem
            rem = 0
            if s >= 10:
                rem = 1
                print(s)
                node.val = s % 10
            else:
                node.val = s
            
            up = up.next
            down = down.next
            res = res.next
        if rem > 0:
            if up:
                while up:
                    node = ListNode()
                    res.next = node
                    s = up.val + rem
                    rem = 0
                    if s >= 10:
                        rem = 1
                        #print(s)
                        node.val = s % 10
                    else:
                        node.val = s
                    
                    up = up.next
                    res = res.next
            elif down:
                while down:
                    node = ListNode()
                    res.next = node
                    s = down.val + rem
                    rem = 0
                    if s >= 10:
                        rem = 1
                        #print(s)
                        node.val = s % 10
                    else:
                        node.val = s

                    down = down.next
                    res = res.next
        if rem > 0:
            res.next = ListNode(1)
        if up:
            res.next = up
        elif down:
            res.next = down
        return dumb.next