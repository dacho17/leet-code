from RomanToInteger import transformRomanToDecimal

class TestSuite:
    def test_1(self):
        return transformRomanToDecimal("X") == 10
    def test_2(self):
        return transformRomanToDecimal("XIII") == 13
    def test_3(self):
        return transformRomanToDecimal("XIV") == 14
    def test_4(self):
        return transformRomanToDecimal("CDXXXIV") == 434
    def test_5(self):
        return transformRomanToDecimal("XLIV") == 44
    def test_6(self):
        return transformRomanToDecimal("MCMXCIV") == 1994
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
