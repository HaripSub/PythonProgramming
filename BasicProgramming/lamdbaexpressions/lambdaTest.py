import unittest
import lambda_basic_examples


class MyTestCase(unittest.TestCase):
    def test_lambda_sum_function(self):
        sum = lambda_basic_examples.add(6, 9)
        self.assertEqual(sum, 15)

    def test_lambda_maximum_two_function(self):
        maximum = lambda_basic_examples.maximum_two_numbers(6, 9)
        self.assertEqual(maximum, 9)

    def test_lambda_factorial_function(self):
        factorial = lambda_basic_examples.factorial_num(6)
        self.assertEqual(factorial, 720)

    def test_lambda_square(self):
        square = lambda_basic_examples.square_num(5)
        self.assertEqual(square, 25)

    def test_find_maximum_list_lambda(self):
        given_list = [23, 89, 56, 45, 67]
        maximum_list = lambda_basic_examples.find_max_numbers_list(given_list)
        self.assertEqual(maximum_list, 89)

    def test_is_prime_true(self):
        is_prime = lambda_basic_examples.is_prime(7)
        self.assertEqual(is_prime, "The 7 is prime");

    def test_is_prime_false(self):
        is_prime = lambda_basic_examples.is_prime(12)
        self.assertEqual(is_prime, "The 12 is not prime");


if __name__ == '__main__':
    unittest.main()
