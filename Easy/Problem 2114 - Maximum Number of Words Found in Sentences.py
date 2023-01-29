import unittest

class Solution:
    def mostWordsFound(self, sentences):
        result = 0
        for i in sentences:
            data = i.split()
            if len(data) > result:
                result = len(data)
            
        return result
    
class Test(unittest.TestCase):
    def test_One(self):
        sentences = ["alice and bob love leetcode","i think so too","this is great thanks very much"]
        test = Solution.mostWordsFound(self, sentences)
        self.assertEqual(test, 6, "Error")
    
    def test_Two(self):
        sentences = ["please wait", "continue to fight", "continue to win"]
        test = Solution.mostWordsFound(self, sentences)
        self.assertEqual(test, 3, "Error")
        

unittest.main()