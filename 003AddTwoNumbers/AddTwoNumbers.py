class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(firstNum: ListNode, secondNum: ListNode):
    carryOver = 0
    res = ListNode()
    cur = res
    while firstNum != None or secondNum != None:
        digitSum = cur.val
        if firstNum != None:
            digitSum += firstNum.val
            firstNum = firstNum.next
        if secondNum != None:
            digitSum += secondNum.val
            secondNum = secondNum.next
        cur.val = digitSum % 10

        carryOver = 1 if digitSum > 9 else 0
        if carryOver == 1 or firstNum != None or secondNum != None:
            cur.next = ListNode(carryOver)
            cur = cur.next
    
    return res
