from ReverseInteger import reverseInteger

class TestSuite:
    def test_1(self):
        return reverseInteger(0) == 0
    def test_2(self):
        return reverseInteger(9) == 9
    def test_3(self):
        return reverseInteger(11) == 11
    def test_4(self):
        return reverseInteger(31) == 13
    def test_5(self):
        return reverseInteger(120) == 21
    def test_6(self):
        return reverseInteger(-12030) == -3021

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
