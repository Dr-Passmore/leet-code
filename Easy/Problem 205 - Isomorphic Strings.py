import unittest
import collections
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        output1 = []
        output2 = [] 
        for i in s:
            sleepy = s.index(i)
            output1.append(sleepy)
        for i in t: 
            sleepy = t.index(i)
            output2.append(sleepy)
            
        if output1 == output2:
            return True
        
        else:
            return False
            
                
            
        
        '''countofS = list(collections.Counter(s).values())
        
        countofT = list(collections.Counter(t).values())
        
        if countofT == countofS:
            return True
        
        else: 
            return False
           ''' 
        
class Test(unittest.TestCase):
    def test_case1(self):
        test = Solution.isIsomorphic(self,"egg", "add")
        self.assertEqual(test, True, "Error")
    
    def test_case2(self):
        test = Solution.isIsomorphic(self, "foo", "bar")
        self.assertEqual(test, False, "Error")
        
    def test_case3(self):
        test = Solution.isIsomorphic(self, "paper", "title")
        self.assertEqual(test, True, "Error")
        
    def test_case4(self):
        test = Solution.isIsomorphic(self, "bbbaaaba", "aaabbbba")
        self.assertEqual(test, False, "Error")
        
        
unittest.main()
    