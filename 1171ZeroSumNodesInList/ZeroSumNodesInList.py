# Create a dictionary with entry of format (prefixSum, node) where prefixSum is a prefixSum up to node.
# Iterate through list and store prefixSums with nodes to a dictionary.
# If the prefixSum has already been seen remove all those nodes from the dictionary which come between the current node
# and the node to which prefix sum points (both included).
# Connect the prefixSum to the follower node of the current node.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head: ListNode):
    prefixSum = 0
    sumNodes = { prefixSum: head }
    cur = head
    while cur != None:
        prefixSum += cur.val
        if prefixSum in sumNodes:
            nodeToRemove = sumNodes[prefixSum]
            prefixSumToDel = prefixSum
            while prefixSumToDel != prefixSum:
                del sumNodes[prefixSumToDel]
                prefixSumToDel += nodeToRemove.val
                nodeToRemove = sumNodes[prefixSumToDel]
        sumNodes[prefixSum] = cur.next
        cur = cur.next

    prefixSum = 0
    currentNode = sumNodes[prefixSum]
    while currentNode != None:
        prefixSum += currentNode.val
        currentNode.next = sumNodes[prefixSum]
        currentNode = currentNode.next
    return sumNodes[0]

def serialize(node: ListNode):
    sol = []
    while node != None:
        sol.append(node.val)
        node = node.next
    return sol
