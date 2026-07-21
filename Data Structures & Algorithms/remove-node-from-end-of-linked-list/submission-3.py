class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        pos = length - n

        # Delete head
        if pos == 0:
            return head.next

        temp = head
        count = 0

        while count < pos - 1:
            temp = temp.next
            count += 1

        temp.next = temp.next.next

        return head