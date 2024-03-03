class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthNode(lst, n):
    listLength = getLengthOfList(lst)
    if n > listLength:
        return lst
    if n == listLength:
        return lst.next

    cur = lst
    curIndex = 0
    while cur != None:
        if curIndex + 1 == listLength - n:
            cur.next = cur.next.next
            break
        curIndex += 1
        cur = cur.next
    
    return lst


def getLengthOfList(lst):
    length = 0
    while lst != None:
        lst = lst.next
        length += 1
    return length

def toList(lst):
    sol = []
    while lst != None:
        sol.append(lst.val)
        lst = lst.next
    return sol
