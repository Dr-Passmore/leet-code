import unittest

class Solution:
    def restoreString(self, s: str, indices) -> str:
        
        output = ["*" for i in range(len(s))]
        for indices, v in enumerate(indices):
            output[v] = s[indices]
            print(output)
        
        return "".join(output)
            
        
            
            
        
class Test(unittest.TestCase):
    def test_case1(self):
        test = Solution.restoreString(self, "codeleet", [4,5,6,7,0,2,1,3])
        self.assertEqual(test, "leetcode", "Error")
    
    def test_case2(self):
        test = Solution.restoreString(self, "abc", [0,1,2])
        self.assertEqual(test, "abc", "Error")


unittest.main()