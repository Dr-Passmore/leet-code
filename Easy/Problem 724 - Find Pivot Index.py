import unittest
class Solution:
    def pivotIndex(self, nums):
        for i, v in enumerate (nums):
            
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
           
            
        return -1
            
            
    
class Test(unittest.TestCase):
    def test_case1(self):
        test = Solution.pivotIndex(self,[1,7,3,6,5,6])
        self.assertEqual(test, 3, "Error")
    
    def test_case2(self):
        test = Solution.pivotIndex(self, [1,2,3])
        self.assertEqual(test, -1, "Error")
        
    def test_case3(self):
        test = Solution.pivotIndex(self, [2,1,-1])
        self.assertEqual(test, 0, "Error")
        
unittest.main()
    