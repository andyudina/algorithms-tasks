"""
Write an efficient function that takes stock prices and returns the best profit one could have made from one purchase and one sale of one share.
Stock prices are stored in a list
"""
import unittest


def get_max_profit_simple(stock_prices):
    """
    Accepts list of stock prices.
    Returns the biggest difference between two individual prices
    Prices are in order: minimum price should go before maximum price 
    in an array

    Simple implementaton uses O^2 algorythm with double for loops
    """
    assert len(stock_prices) > 0, \
      'Stock prices list can not be empty'
    value_diff = stock_prices[len(stock_prices) - 1] - \
                 stock_prices[0]
    for i in range(len(stock_prices) - 1):
        for j in range(i + 1, len(stock_prices)):
            curr_value = stock_prices[j] - stock_prices[i]
            if curr_value > value_diff:
                value_diff = curr_value
    return value_diff


class TestGetMaxProfitFunctionMixin(object):
    """
    Test mixin wich defines all sorts of test
    we want to run with inddividual "get_max_profit"
    implementation
    """

    def test_max_profit_is_correct__min_and_max_element_is_diff_halves(self):
        """
        We return correct max profit value
        when maximum element in second half and minimum element in first half
        """
        stock_prices = [10, 7, 5, 8, 11, 9]
        self.assertEqual(
            self.get_max_profit(stock_prices),
            6)

    def test_max_profit_is_correct__min_and_max_element_is_first_half(self):
        """
        We return correct max profit value
        when maximum and minimum element are in first half
        """
        stock_prices = [5, 7, 11, 4, 8, 9]
        self.assertEqual(
            self.get_max_profit(stock_prices),
            6)

    def test_max_profit_is_correct__min_and_max_element_is_second_half(self):
        """
        We return correct max profit value
        when maximum and minimum element are in second half
        """
        stock_prices = [10, 7, 8, 4, 11, 9]
        self.assertEqual(
            self.get_max_profit(stock_prices),
            7)

    def test_max_profit_is_correct__odd_elements_number(self):
        """
        We return correct max profit value
        when there is odd elements number in array
        """
        stock_prices = [10, 7, 4, 10, 8, 11, 9]
        self.assertEqual(
            self.get_max_profit(stock_prices),
            7)

    def test_stock_list_with_one_element(self):
        """
        We return correct max profit value
        when list has only one element
        """
        stock_prices = [10]
        self.assertEqual(
            self.get_max_profit(stock_prices),
            0)

    def test_stock_list_with_equal_elements(self):
        """
        We return correct max profit value
        when list has same elements
        """
        stock_prices = [10, 10, 10]
        self.assertEqual(
            self.get_max_profit(stock_prices),
            0)

    def test_stock_list_with_zero_elements(self):
        """
        We raise error if list is empty
        """
        with self.assertRaises(AssertionError):
            self.get_max_profit([])


class TestGetMaxProfitFunctionSimple(
        TestGetMaxProfitFunctionMixin,
        unittest.TestCase):
    """
    Test simmple implementation of get_max_profi_function
    with double loops
    """

    def get_max_profit(self, stock_prices):
        return get_max_profit_simple(stock_prices)

if __name__ == '__main__':
    unittest.main()
