import unittest
import itertools
class Solution:
    def minimumSum(self, num):
        values = ["".join(i) for i in itertools.permutations(str(num), 4)]
        minoutput = 10000
        print(values)
        for i in values:
            if (int(i[0:2]) + (int(i[2:]))) < minoutput:
                minoutput = int(i[0:2]) + (int(i[2:]))
            
        return minoutput
    
class Test(unittest.TestCase):
    def test_One(self):
        num = 2932
        test = Solution.minimumSum(self, num)
        self.assertEqual(test, 52, "Error")
    
    def test_Two(self):
        num = 4009
        test = Solution.minimumSum(self, num)
        self.assertEqual(test, 13, "Error")
        

unittest.main()