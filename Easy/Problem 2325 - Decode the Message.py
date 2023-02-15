import unittest
import string
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = list(string.ascii_lowercase)
        print(key)
        unquekey = []
        for i in key:
            if i not in unquekey and i != " ":
                unquekey.append(i)
            else:
                continue
        
        
        codeLookUp = dict(zip(unquekey, alphabet))
        print(codeLookUp)
        output = []
        for i in message:
            if i == " ":
                output.append(i)
            else:
                output.append(codeLookUp[i])
        print("".join(output))
        return "".join(output) 
        
        
        
class Test(unittest.TestCase):
    def test_case1(self):
        test = Solution.decodeMessage(self,"the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv")
        self.assertEqual(test, "this is a secret", "Error")
    
    def test_case2(self):
        test = Solution.decodeMessage(self, "eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb")
        self.assertEqual(test, "the five boxing wizards jump quickly", "Error")
        


unittest.main()