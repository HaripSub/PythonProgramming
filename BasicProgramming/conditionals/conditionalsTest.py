import unittest
from datetime import date
from conditionals import conditionals1
from conditionals2 import check_guess
from conditionals3 import triangle_type


class ConditionalsTest(unittest.TestCase):
    def test_valid_age(self):
        # Test for a person who is old enough to vote
        birth_year = date.today().year - 20
        expected_result = "Congrats. You are allowed to vote"
        self.assertEqual(conditionals1.check_validity_to_vote(birth_year), expected_result)

    def test_invalid_age(self):
        # Test for a person who is too young to vote
        birth_year = date.today().year - 10
        expected_result = "Sorry. You are too young to vote"
        self.assertEqual(conditionals1.check_validity_to_vote(birth_year), expected_result)

    def test_invalid_input(self):
        # Test for invalid input (non-numeric birth year)
        birth_year = "abcd"
        expected_result = "Invalid input. Please enter a valid birth year as a number."
        self.assertEqual(conditionals1.check_validity_to_vote(birth_year), expected_result)

    def test_custom_voting_age(self):
        # Test with a custom voting age
        birth_year = date.today().year - 16
        voting_age = 21
        expected_result = "Sorry. You are too young to vote"
        self.assertEqual(conditionals1.check_validity_to_vote(birth_year, voting_age), expected_result)

    def test_correct_guess(self):
        self.assertEqual(check_guess(50, 50), "Correct!")

    def test_too_low_guess(self):
        self.assertEqual(check_guess(50, 30), "Too low! Try again.")

    def test_too_high_guess(self):
        self.assertEqual(check_guess(50, 70), "Too high! Try again.")

    def test_out_of_range_guess_low(self):
        self.assertEqual(check_guess(50, 0), "Please guess a number within the range 1 to 100.")

    def test_out_of_range_guess_high(self):
        self.assertEqual(check_guess(50, 101), "Please guess a number within the range 1 to 100.")

    def test_equilateral_triangle(self):
        self.assertEqual(triangle_type(5, 5, 5), "Equilateral")

    def test_isosceles_triangle(self):
        self.assertEqual(triangle_type(5, 5, 8), "Isosceles")
        self.assertEqual(triangle_type(5, 8, 5), "Isosceles")
        self.assertEqual(triangle_type(8, 5, 5), "Isosceles")

    def test_scalene_triangle(self):
        self.assertEqual(triangle_type(3, 4, 5), "Scalene")

    def test_not_a_triangle(self):
        self.assertEqual(triangle_type(1, 1, 3), "Not a triangle")
        self.assertEqual(triangle_type(1, 2, 3), "Not a triangle")
        self.assertEqual(triangle_type(10, 1, 1), "Not a triangle")


if __name__ == '__main__':
    unittest.main()
