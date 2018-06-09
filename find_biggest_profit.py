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

    Simple implementaton uses O(n^2) algorythm with double for loops
    """
    assert len(stock_prices) > 1, \
      'Stock prices list can not be empty'
    value_diff = stock_prices[len(stock_prices) - 1] - \
                 stock_prices[0]
    for i in xrange(len(stock_prices) - 1):
        for j in xrange(i + 1, len(stock_prices)):
            curr_value = stock_prices[j] - stock_prices[i]
            if curr_value > value_diff:
                value_diff = curr_value
    return value_diff

def get_max_profit_greedy(stock_prices):
    """
    Accepts list of stock prices.
    Returns the biggest difference between two individual prices
    Prices are in order: minimum price should go before maximum price 
    in an array

    Simple implementaton uses O(1) algorythm with one time going through array
    """
    assert len(stock_prices) > 1, \
      'Stock prices list must have more than one element'

    min_price  = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]
    for current_index in xrange(1, len(stock_prices)):
        current_price = stock_prices[current_index]
        current_profit = current_price - min_price
        max_profit = max(max_profit, current_profit)
        min_price  = min(min_price, current_price)
    return max_profit

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

    def test_stock_list_with_equal_elements(self):
        """
        We return correct max profit value
        when list has same elements
        """
        stock_prices = [10, 10, 10]
        self.assertEqual(
            self.get_max_profit(stock_prices),
            0)

    def test_stock_list__last_element_is_minimum(self):
        """
        We return correct max profit value
        when list has global minimum in last place
        """
        stock_prices = [8, 9, 5, 6, 3]
        self.assertEqual(
            self.get_max_profit(stock_prices),
            1)

    def test_stock_list__minimum_element_after_best_pair(self):
        """
        We return correct max profit value
        when list has global minimum element after best fait
        """
        stock_prices = [5, 11, 3, 4]
        self.assertEqual(
            self.get_max_profit(stock_prices),
            6)

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
    Test simple implementation of get_max_profit_function_simpe
    with double loops
    """

    def get_max_profit(self, stock_prices):
        return get_max_profit_simple(stock_prices)


class TestGetMaxProfitFunction(
        TestGetMaxProfitFunctionMixin,
        unittest.TestCase):
    """
    Test greedy implementation of get_max_profi_function
    with double loops
    """

    def get_max_profit(self, stock_prices):
        return get_max_profit_greedy(stock_prices)


if __name__ == '__main__':
    unittest.main()
