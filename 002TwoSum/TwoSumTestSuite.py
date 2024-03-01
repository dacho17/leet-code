from TwoSum import twoSum

class TestSuite:
    def test_1(self):
        return twoSum([2, 7, 11, 15], 9) == [0, 1]
    def test_2(self):
        return twoSum([3, 2, 4], 7) == [0, 2]
    def test_3(self):
        return twoSum([3, 3], 6) == [0, 1]
    def test_4(self):
        return twoSum([2, 7, 11, 15], 18) == [1, 2]
    def test_5(self):
        return twoSum([2, 7, 11, 15, 13, 26], 15) == [0, 4]
    def test_6(self):
        return twoSum([1, 2, 3, 4, 5, 6], 11) == [4, 5]
    def return_test_result(self, test_func):
        return "Passed" if test_func() == True else "Failed"

    def run_test_suite(self):
        print("Test results:")
        print("Test_1 : " + self.return_test_result(self.test_1))
        print("Test_2 : " + self.return_test_result(self.test_2))
        print("Test_3 : " + self.return_test_result(self.test_3))
        print("Test_4 : " + self.return_test_result(self.test_4))
        print("Test_5 : " + self.return_test_result(self.test_5))
        print("Test_6 : " + self.return_test_result(self.test_6))
        print("Test suite finished running")
