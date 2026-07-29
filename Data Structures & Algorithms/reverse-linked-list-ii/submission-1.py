# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        val=[]
        temp=head
        count=1
        while count<left and temp.next is not None:
            temp=temp.next
            count+=1
        lefthead=temp
        while left<right+1:
            val.append(temp.val)
            temp=temp.next
            left+=1
        val=val[::-1]
        temp=lefthead
        for i in range(len(val)):
            temp.val=val[i]
            temp=temp.next
        return head

        