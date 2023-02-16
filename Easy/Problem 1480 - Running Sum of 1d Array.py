import unittest
class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums [i-1] + nums[i]
        return nums
        
class Test(unittest.TestCase):
    def test_case1(self):
        test = Solution.runningSum(self,[1,2,3,4])
        self.assertEqual(test, [1,3,6,10], "Error")
    
    def test_case2(self):
        test = Solution.runningSum(self, [1,1,1,1,1])
        self.assertEqual(test, [1,2,3,4,5], "Error")
        
    def test_case3(self):
        test = Solution.runningSum(self, [3,1,2,10,1])
        self.assertEqual(test, [3,4,6,16,17], "Error")
        
unittest.main()