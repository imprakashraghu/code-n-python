# Given the head of a singly linked list, reverse the list, and return the reversed list.

# 1 -> 2 -> 3 -> 4 -> 5 -> null
# 5 -> 4 -> 3 -> 2 -> 1 -> null

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
        
    cur = head
    tail = None

    while cur:
        temp = cur.next
        
        cur.next = tail
        tail = cur

        cur = temp

    return tail