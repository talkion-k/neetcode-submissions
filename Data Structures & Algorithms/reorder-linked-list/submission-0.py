# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def recList(base, curr):
            # need recList to go down layers until it reaches the last node
            # then, link the "base" (first) node to the last node and go up
            # before it goes up, increment the "base" node
            if not curr: # if end of list is reached
                return base
            base = recList(base, curr.next)
            if not base: # if list is empty
                return None
            if base == curr or base.next == curr:
                curr.next = None
                return None
            else:
                # link curr to base
                temp = base.next
                base.next = curr
                curr.next = temp
                return temp
        head = recList(head, head.next)

                