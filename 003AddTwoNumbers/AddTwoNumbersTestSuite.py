# TODO: this suite needs to be rewritten to work with ListNodes

from AddTwoNumbers import addTwoNumbers, ListNode

class TestSuite:
    def test_1(self):
        return addTwoNumbers(ListNode(0), ListNode(0, ListNode(1))) == [0, 1]
    def test_2(self):
        return addTwoNumbers([5], [5]) == [0, 1]
    def test_3(self):
        return addTwoNumbers([2, 4, 3], [5, 6, 4]) == [7, 0, 8]
    def test_4(self):
        return addTwoNumbers([9,9,9,9,9,9,9], [9, 9, 9, 9]) == [8,9,9,9,0,0,0,1]
    def test_5(self):
        return addTwoNumbers([6, 6, 6], [4, 4, 4]) == [0, 1, 1, 1]
    def test_6(self):
        return addTwoNumbers([0], [0]) == [0]

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
