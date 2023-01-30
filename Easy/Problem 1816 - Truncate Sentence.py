import unittest

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        data = s.split()
        newstr = []
        
        for i in data[:int(k)]:
            newstr.append(i)
        result = " ".join(newstr)
        return result
        
class Test(unittest.TestCase):
    def test_case1(self):
        test = Solution.truncateSentence(self,"Hello how are you Contestant", 4)
        self.assertEqual(test, "Hello how are you", "Error")
    
    def test_case2(self):
        test = Solution.truncateSentence(self, "What is the solution to this problem", 4)
        self.assertEqual(test, "What is the solution", "Error")
        
    def test_case3(self):
        test = Solution.truncateSentence(self,"chopper is not a tanuki", 5)
        self.assertEqual(test, "chopper is not a tanuki" , "Error")


unittest.main()