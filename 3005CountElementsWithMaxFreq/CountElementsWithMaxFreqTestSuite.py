from CountElementsWithMaxFreq import countElsWithMaxFreq

class TestSuite:
    def test_1(self):
        return countElsWithMaxFreq([1]) == 1
    def test_2(self):
        return countElsWithMaxFreq([0, 1]) == 2
    def test_3(self):
        return countElsWithMaxFreq([0, 1, 0]) == 2
    def test_4(self):
        return countElsWithMaxFreq([1, 2, 2, 3, 1, 4]) == 4
    def test_5(self):
        return countElsWithMaxFreq([1, 2, 3, 4, 5]) == 5
    def test_6(self):
        return countElsWithMaxFreq([0, 1, 0, 1, 0, 1, 4]) == 6
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
