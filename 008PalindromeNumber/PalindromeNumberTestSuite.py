from PalindromeNumber import isPalindrome

class TestSuite:
    def test_1(self):
        return isPalindrome(1) == True
    def test_2(self):
        return isPalindrome(11) == True
    def test_3(self):
        return isPalindrome(12) == False
    def test_4(self):
        return isPalindrome(123) == False
    def test_5(self):
        return isPalindrome(121) == True
    def test_6(self):
        return isPalindrome(12321) == True
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
