import unittest

class Solution:
    def countAsterisks(self, s: str) -> int:
        data = s.split("|")
        print(data)
        position = 1
        count = 0
        for i in data:
            if position % 2 != 0:
                num = i.count('*')
                count += num
            position += 1
        return count
                
                
        
        
        
class Test(unittest.TestCase):
    def test_case1(self):
        test = Solution.countAsterisks(self,"l|*e*et|c**o|*de|")
        self.assertEqual(test, 2, "Error")
    
    def test_case2(self):
        test = Solution.countAsterisks(self, "iamprogrammer")
        self.assertEqual(test, 0, "Error")
        
    def test_case3(self):
        test = Solution.countAsterisks(self,"yo|uar|e**|b|e***au|tifu|l")
        self.assertEqual(test, 5 , "Error")


unittest.main()