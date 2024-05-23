import unittest
import functions


class MyTestCase(unittest.TestCase):
    def test_addition(self):
        sum = functions.addition(5, 7)
        self.assertEqual(sum, 12)


if __name__ == '__main__':
    unittest.main()
