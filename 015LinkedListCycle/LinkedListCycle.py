class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(lst):
    slowPtr, fastPtr = lst, lst
    while fastPtr != None and fastPtr.next != None:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
        if fastPtr == slowPtr:
            return True
    return False
