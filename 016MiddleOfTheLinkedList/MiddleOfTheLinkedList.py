class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(lst):
    length = listLength(lst)
    middleNodeIndex = length // 2
    curIndex = 0
    while lst != None:
        if middleNodeIndex == curIndex:
            return lst
        curIndex += 1
        lst = lst.next
    return -1


def listLength(lst):
    sol = 0
    while lst != None:
        sol += 1
        lst = lst.next
    return sol
