import unittest
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        check= []
        drunkBear = 0
        stilldrunkbear = 0
        
        while drunkBear < len(s) and stilldrunkbear < len(t):
            if s[drunkBear] == t[stilldrunkbear]:
                check.append(t[stilldrunkbear])
                drunkBear += 1
                stilldrunkbear += 1
            else:
                stilldrunkbear += 1
        
        print(check)
        if check == list(s):
            return True
        else:
            return False
        
class Test(unittest.TestCase):
    def test_case1(self):
        test = Solution.isSubsequence(self,"abc", "ahbgdc")
        self.assertEqual(test, True, "Error")
    
    def test_case2(self):
        test = Solution.isSubsequence(self, "axc", "ahbgdc")
        self.assertEqual(test, False, "Error")
        
    def test_case3(self):
        test = Solution.isSubsequence(self, "acb", "ahbgdc")
        self.assertEqual(test, False, "Error")
        
unittest.main()