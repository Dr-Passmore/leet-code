

import unittest

class Solution:
    def mergeTwoLists(self, list1, list2):
        newHead = dummyHead = ListNode()
        
        mergedlist = list(list1) + list(list2)
        mergedlist.sort()
        return mergedlist
        

class Test(unittest.TestCase):
    def test_normal_case(self):
        test = Solution.mergeTwoLists(self,[1,2,4], [1,3,4])
        self.assertEqual(test, [1,1,2,3,4,4], "Error")
    
    def test_ordered(self):
        test = Solution.mergeTwoLists(self,[], [])
        self.assertEqual(test, [], "Error")
        
    def test_unordered(self):
        test = Solution.mergeTwoLists(self,[], [0])
        self.assertEqual(test, [0], "Error")


unittest.main()