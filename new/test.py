import unittest
import addFunc
from unittest import mock
 
class MyCalcTest(unittest.TestCase):
    @mock.patch("addFunc.add")
    def test_add(self, mock_add):
        num=50
        mock_add.return_value=num
        c = addFunc.add(20, 10)
        self.assertEqual(c, num)
 
if __name__ == '__main__':
    unittest.main()