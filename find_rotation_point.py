"""
Task: find index of "rotation point" in a list of words. 
List starts in reversed alphabetical order and continues in alphabetical order.
We need to find index of the word where order change occures
"""
import unittest


def find_rotation_point(list_):
    """
    Find rotation point in list of words, where first part is
    in reversed alphabetical order and second part is in normal order
    Uses O(n) time
    """
    assert len(list_) >= 3, \
        "List should have at least 3 words"
    index = 1
    # iterate over list_[1:-1]
    while (index < len(list_) - 1):
        # assume we don't have same words in a list
        if list_[index] < list_[index - 1] and \
           list_[index] < list_[index + 1]:
            # rotation point should be "earlier" in the alphabetic order
            # than both previous and next item
            return index
        index += 1
    # no rotation points found
    # list is sorted in one direction
    return None


class TestFindRotationPoint(
        unittest.TestCase):
    """
    Test find_rotation_point function
    """

    def test_rotation_point_found(self):
        """
        We return valid rotation point
        """
        self.assertEqual(
            find_rotation_point([
                'ptolemaic',
                'retrograde',
                'supplant',
                'undulate',
                'xenoepist',
                'asymptote',  # <-- rotates here!
                'babka',
                'banoffee',
                'engender',
                'karpatka',
                'othellolagkage',
            ]),
            5)

    def test_list_in_alphabetical_order(self):
        """
        We return None if all list is sorted
        in alphabetical order
        """
        self.assertIsNone(
            find_rotation_point([
                'asymptote',
                'babka',
                'banoffee',
                'engender',
                'karpatka',
                'othellolagkage',
            ]))

    def test_list_in_reversed_alphabetical_order(self):
        """
        We return None if all list is sorted
        in reversed alphabetical order
        """
        self.assertIsNone(
            find_rotation_point([
                'ptolemaic',
                'retrograde',
                'supplant',
                'undulate',
                'xenoepist',
            ]))

    def test_list_with_less_than_three_elements(self):
        """
        We raise AssertionError if list has lest than 3 elements
        """
        with self.assertRaises(AssertionError):
            find_rotation_point(['test',])


if __name__ == '__main__':
    unittest.main()
