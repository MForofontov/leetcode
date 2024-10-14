from typing import Optional

class ListNode:
    """
    A node in a singly-linked list.

    Attributes
    ----------
    val : int
        The value of the node.
    next : Optional[ListNode]
        The next node in the linked list.
    """
    def __init__(self, val=0, next=None):
        """
        Initializes a ListNode.

        Parameters
        ----------
        val : int, optional
            The value of the node (default is 0).
        next : Optional[ListNode], optional
            The next node in the linked list (default is None).
        """
        self.val = val
        self.next = next

class Solution:
    """
    A class used to represent the solution for adding two numbers represented by linked lists.
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented by linked lists. Each node contains a single digit and the digits are stored in reverse order.

        Parameters
        ----------
        l1 : Optional[ListNode]
            The first linked list.
        l2 : Optional[ListNode]
            The second linked list.

        Returns
        -------
        Optional[ListNode]
            A linked list representing the sum of the two numbers.
        """
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry, digit = divmod(total, 10)

            current.next = ListNode(digit)
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy_head.next