import unittest
import  cap 
class testcap(unittest.TestCase):
    def test_one_word(self):
        text='python'
        result= cap.cap_test(text)
        self.assertEqual(result,'Python')
    def test_mulitple_words(self):
        text= 'kewal python'
        result= cap.cap_test(text)
        self.assertEqual(result,'Kewal Python')
if __name__== '__main__':
    unittest.main()