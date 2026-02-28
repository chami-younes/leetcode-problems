# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        f_head = ListNode(0)
        f_head.next = head
        prev = head
        cur = head.next

        while cur:
            if cur.val >= prev.val:
                prev = cur
                cur = cur.next
            else:
                # Find where to insert cur
                tmp = f_head
                while tmp.next and tmp.next.val < cur.val:
                    tmp = tmp.next
                
                # Remove cur from current position
                prev.next = cur.next
                
                # Insert cur after tmp
                cur.next = tmp.next
                tmp.next = cur
                
                # Move cur forward
                cur = prev.next
        
        return f_head.next
