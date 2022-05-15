class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Fast and Slow Pointer
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
        # Fast and Slow Pointer

        # Convert to Array
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)

        return arr[len(arr) // 2]
        # Convert to Array