import unittest
from main import DecimalToOctal
 
class TestDecimalToOctal(unittest.TestCase):

    def test_success(self):
        self.assertEquals(DecimalToOctal(10),'12') #success 

    def test_failed(self):
        self.assertEquals(DecimalToOctal(10),'14') #failed

if __name__ == '__main__':
    unittest.main()