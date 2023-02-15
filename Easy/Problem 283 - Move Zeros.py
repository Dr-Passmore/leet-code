import unittest

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for v in nums:
            if v == 0:
                nums.append(nums.pop(nums.index(v)))
                
        return nums
                
class Test(unittest.TestCase):
    def test_case1(self):
        test = Solution.moveZeroes(self,[0,1,0,3,12])
        self.assertEqual(test, [1,3,12,0,0], "Error")
    
    def test_case2(self):
        test = Solution.moveZeroes(self, [0])
        self.assertEqual(test, [0], "Error")
        
unittest.main()