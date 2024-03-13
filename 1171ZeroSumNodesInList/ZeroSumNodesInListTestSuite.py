from ZeroSumNodesInList import ListNode, removeZeroSumSublists, serialize

class TestSuite:
    def test_1(self):
        lst = ListNode(1, ListNode(2, ListNode(-3, ListNode(3, ListNode(1)))))
        return serialize(removeZeroSumSublists(lst)) == [3, 1]
    def test_2(self):
        lst = ListNode(1, ListNode(2, ListNode(3, ListNode(-3, ListNode(4)))))
        return serialize(removeZeroSumSublists(lst)) == [1, 2, 4]
    def test_3(self):
        lst = ListNode(1, ListNode(2, ListNode(3, ListNode(-3, ListNode(-2)))))
        return serialize(removeZeroSumSublists(lst)) == [1]
    def test_4(self):
        lst = ListNode(1, ListNode(2))
        return serialize(removeZeroSumSublists(lst)) == [1, 2]
    def test_5(self):
        lst = ListNode(1, ListNode(-1))
        return serialize(removeZeroSumSublists(lst)) == []
    def test_6(self):   
        [2,-1,-1,2,1,-2]
        lst = ListNode(2, ListNode(-1, ListNode(-1, ListNode(2, ListNode(1, ListNode(-2))))))
        return serialize(removeZeroSumSublists(lst)) == [2, 1, -2]

    def return_test_result(self, test_func):
        return "Passed" if test_func() else "Failed"

    def run_test_suite(self):
        print("Test results:")
        print("Test_1 : " + self.return_test_result(self.test_1))
        print("Test_2 : " + self.return_test_result(self.test_2))
        print("Test_3 : " + self.return_test_result(self.test_3))
        print("Test_4 : " + self.return_test_result(self.test_4))
        print("Test_5 : " + self.return_test_result(self.test_5))
        print("Test_6 : " + self.return_test_result(self.test_6))
        print("Test suite finished running")
