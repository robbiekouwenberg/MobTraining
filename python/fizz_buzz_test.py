# import unittest

from fizz_buzz import FizzBuzz

def test_fizz_buzz_returns_1_for_1():
    fizz_buzz = FizzBuzz()
    assert fizz_buzz.fizz_buzz(1) == "1"

# class FizzBuzzTests(unittest.TestCase):
#     def setUp(self) -> None:
#         self.fizz_buzz = FizzBuzz()

#     def test_writes_correct_output_for_count(self):
#         self.assertEqual(self.fizz_buzz.fizz_buzz(16), "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16")

# # if __name__ == '__main__':
# #     unittest.main()