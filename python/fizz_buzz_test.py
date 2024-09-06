from fizz_buzz import FizzBuzz

def test_writes_correct_output_for_count_1():
    assert FizzBuzz().fizz_buzz(1) == "1"
    
def test_writes_correct_output_for_count_3():
    assert FizzBuzz().fizz_buzz(1) == "1, 2, Fizz"

def test_writes_correct_output_for_count_5():
    assert FizzBuzz().fizz_buzz(1) == "1, 2, Fizz, 4, Buzz,"

def test_writes_correct_output_for_count_15():
    assert FizzBuzz().fizz_buzz(1) == "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz"

def test_writes_correct_output_for_count_16():
    assert FizzBuzz().fizz_buzz(1) == "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16"