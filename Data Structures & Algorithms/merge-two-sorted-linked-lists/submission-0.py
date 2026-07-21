# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return list1
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        temp1=list1
        temp2=list2
        if temp1.val<=temp2.val:
            
            head=temp1
            prev=temp1
            temp1=temp1.next
        else:
            head=temp2
            prev=temp2
            temp2=temp2.next
        while temp1 is not None and temp2 is not None:
            if temp1.val<=temp2.val:
                head.next=temp1
                head=head.next
                temp1=temp1.next
            else:
                head.next=temp2
                head=head.next
                temp2=temp2.next
        while temp1 is not None:
            head.next=temp1
            head=head.next
            temp1=temp1.next
        while temp2 is not None:
            head.next=temp2
            head=head.next
            temp2=temp2.next
        return prev
        