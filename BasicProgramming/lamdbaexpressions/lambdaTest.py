import unittest
import lambda_examples


class MyTestCase(unittest.TestCase):
    def test_lambda_sum_function(self):
        sum = lambda_examples.add(6, 9)
        self.assertEqual(sum, 15)

    def test_lambda_maximum_two_function(self):
        maximum = lambda_examples.maximum_two_numbers(6, 9)
        self.assertEqual(maximum, 9)

    def test_lambda_factorial_function(self):
        factorial = lambda_examples.factorial_num(6)
        self.assertEqual(factorial, 720)

    def test_lambda_square(self):
        square = lambda_examples.square_num(5)
        self.assertEqual(square, 25)

    def test_find_maximum_list_lambda(self):
        given_list = [23, 89, 56, 45, 67]
        maximum_list = lambda_examples.find_max_numbers_list(given_list)
        self.assertEqual(maximum_list,89)


if __name__ == '__main__':
    unittest.main()
