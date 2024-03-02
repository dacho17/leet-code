from SquaresOfSortedArray import sortedSquares

class TestSuite:
    def test_1(self):
        return sortedSquares([0]) == [0]
    def test_2(self):
        return sortedSquares([3, 1, 2]) == [1, 4, 9]
    def test_3(self):
        return sortedSquares([-2, 0, 1]) == [0, 1, 4]
    def test_4(self):
        return sortedSquares([1, -3, 4, 2, -5]) == [1, 4, 9, 16, 25]
    def test_5(self):
        return sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    def test_6(self):
        return sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]

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
