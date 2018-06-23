"""
Check if input string is valid palindrome
"""
from collections import Counter
import unittest


def is_palindrome(str_):
    """
    Checks whether any permutation of an input string is a palindrome.
    Returns true if such permutation exists
    """
    assert str_, \
        'String should not be empty'
    # String can be a palindrome if there is only one uneven character
    counter = Counter(str_)
    has_one_uneven_character = False
    for key, value in counter.items():
        # if number of characters is uneven
        if value % 2 != 0:
            if has_one_uneven_character:
                # we just found another uneven character
                return False
            else:
                has_one_uneven_character = True
    return True


class TestValidatePalindromeChecks(
        unittest.TestCase):
    """
    Test is_palindrome function
    """

    def test_valid_palindrome__all_even(self):
        """
        We return True for valid palindrome with all even characters 
        """
        self.assertTrue(
            is_palindrome('ccii'))

    def test_valid_palindrome__one_uneven_character(self):
        """
        We return True for valid palindrome with one uneven character
        """
        self.assertTrue(
            is_palindrome('civvvic'))

    def test_not_a_palindrome(self):
        """
        We return False for non palindrome function
        """
        self.assertFalse(
            is_palindrome('livci'))

    def test_one_character_string(self):
        """
        We return True if string consists of one character
        """
        self.assertTrue(
            is_palindrome('c'))

    def test_empty_string(self):
        """
        We raise AssertionError if empty string passed
        """
        with self.assertRaises(AssertionError):
            is_palindrome('')


if __name__ == '__main__':
    unittest.main()
