import unittest
import utils  

class UtilsTests(unittest.TestCase):
    def test_hasNumbers(self):
        self.assertTrue(utils.hasNumbers("abc123abc"))
        self.assertFalse(utils.hasNumbers("abcabc"))

    def test_intersect(self):
        listA = ["A", "B"]
        listB = ["C", "A"]
        self.assertEqual(utils.intersect(listA,listB), ["A"])

if __name__ == '__main__':
    unittest.main()