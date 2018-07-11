from fizz_Buzz import fizzbuzz
import pytest

def test_fizzbuzz():
    assert fizzbuzz(1) == 1

def test_fizzbuzz_multiple_of3():
    assert fizzbuzz(3) == "Fizz"

def test_fizzbuzz_multiple_of5():
    assert fizzbuzz(5) == "Buzz"
