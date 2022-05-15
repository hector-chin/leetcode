# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    # Two loop
    length = 0
    node = head
    while node:
        node = node.next
        length += 1
        dummy_head = ListNode(0)
        dummy_head.next = head

    node = dummy_head
    for _ in range(length - n):
        node = node.next

    prev = node
    succ = node.next.next
    prev.next = succ

    return dummy_head.next
    # Two loop

    # Single loop
    dummy_head = ListNode(0)
    dummy_head.next = head

    left = dummy_head
    right = dummy_head
    for _ in range(n):
        right = right.next

    while right.next:
        left = left.next
        right = right.next

    prev = left
    succ = left.next.next
    prev.next = succ

    return dummy_head.next

    # Single loop