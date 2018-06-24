"""
Task: You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
"""
import unittest


def find_product_of_other_integers(list_):
    """
    Find product of other integers in a list
    without using division
    Runs O(n) time
    """
    assert len(list_) >= 2, \
        'List should have2 or more elements'
    i = 0
    j = len(list_) - 1
    mult = 1
    res_list = [1, ] * len(list_)
    # We iterate from both sides in the same time.
    # Before iterators reaches the middle element:
    # we multiply all elements that we already saw
    # and save result multipled by element in position of another iterator
    # result is incomplete - we would need to add elements 
    # that we haven't seen yet
    while (i < j):
        res_list[i] = mult * list_[j]
        res_list[j] = mult * list_[i]
        mult *= list_[i] * list_[j]
        i += 1
        j -= 1
    # Lists with even and uneven number of elements behave differently
    # if number of elements is uneven, we would need to replace middle
    # element with multiplication of all others 
    # (what we already have on this stage)
    # and use this value in firther multiplications
    if i == j:
        res_list[i] = mult
        mult = list_[i]
        i += 1
        j -= 1
    else:
        # if number of elements is even,
        # we just flash the multiplication result
        mult = 1
    # after we passed the middle of the list
    # we would need to multiply the resluts by the numbers we
    # missed in the first attempt. We will store them in flashed mult variable
    while (j >= 0):
        res_list[i] = mult * res_list[i]
        res_list[j] = mult * res_list[j]
        mult *= list_[i] * list_[j]
        i += 1
        j -= 1
    return res_list


class TestFindProductOfOtherNumbers(
        unittest.TestCase):
    """
    Test find_product_of_other_integers function
    """

    def test_list_with_even_elements(self):
        """
        We return valid result for list with event number of elements
        """
        self.assertListEqual(
            find_product_of_other_integers([1, 7, 3, 4]),
              [84, 12, 28, 21])

    def test_list_with_uneven_elements(self):
        """
        We return valid result for list with unevent number of elements
        """
        self.assertListEqual(
            find_product_of_other_integers([1, 7, 4, 5, 6, 3, 4]),
              [
                  7 * 4 * 5 * 6 * 3 * 4,
                  1 * 4 * 5 * 6 * 3 * 4,
                  1 * 7 * 5 * 6 * 3 * 4,
                  1 * 7 * 4 * 6 * 3 * 4,
                  1 * 7 * 4 * 5 * 3 * 4,
                  1 * 7 * 4 * 5 * 6 * 4,
                  1 * 7 * 4 * 5 * 6 * 3,
              ])

    def test_list_with_only_two_element(self):
        """
        We return valid result for list with only two elements
        """
        self.assertListEqual(
            find_product_of_other_integers([1, 7]),
              [7, 1])

    def test_list_with_less_than_two_element(self):
        """
        We raise AssertionError if list has lest than 2 elements
        """
        with self.assertRaises(AssertionError):
            find_product_of_other_integers([1,])


if __name__ == '__main__':
    unittest.main()
