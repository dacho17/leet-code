from MaximumOddBinaryNumber import maximumOddBinary

class TestSuite:
    def test_1(self):
        maximumOddBinary("010") == "001"
    def test_2(self):
        maximumOddBinary("0101") == "1001"
    def test_3(self):
        maximumOddBinary("101010") == "110001"
    def test_4(self):
        maximumOddBinary("110000") == "100001"
    def test_5(self):
        maximumOddBinary("100001") == "100001"
    def test_6(self):
        maximumOddBinary("111111") == "111111"
        
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
