from LinkedListCycle import hasCycle, ListNode

class TestSuite:
    def test_1(self):
        return hasCycle(ListNode(0)) == False
    def test_2(self):
        return hasCycle(ListNode(0, ListNode(1))) == False
    def test_3(self):
        return hasCycle(ListNode(0, ListNode(1, ListNode(0)))) == False
    def test_4(self):
        cycle = ListNode(0)
        cycle.next = cycle
        return hasCycle(cycle) == True
    def test_5(self):
        cycle = ListNode(0, ListNode(1))
        cycle.next.next = cycle
        return hasCycle(cycle) == True
    def test_6(self):
        cycle = ListNode(2, ListNode(0, ListNode(-4)))
        cycle.next.next = cycle
        return hasCycle(ListNode(3, cycle)) == True

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
