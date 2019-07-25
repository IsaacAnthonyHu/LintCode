"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        # head是节点地址对应的值，即self.val的感觉
        # 同时还能够调用.next
        
        if head == None:
            return None
        
        slow = head
        fast = head.next # 考虑偶数链表，需要加一
        
        while fast is not None and fast.next is not None:
            
            slow = slow.next
            
            fast = fast.next.next
            
        return slow
            
