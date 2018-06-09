"""
Check weather braces, brackets, and parentheses are balanced
"""
import unittest

def are_braces_brackets_and_parentheses_balanced(str_):
    """
    Validates if braces, brackets, and parentheses
    are properly nested in given str
    """
    OPENING_SYMBOLS = ['{', '[', '(',]
    CLOSING_SYMBOLS = ['}', ']', ')']
    CLOSING_TO_OPENING_MAP = {
      '}': '{',
      ']': '[',
      ')': '('
    }
    stack = []
    for char in str_:
        if char in OPENING_SYMBOLS:
            stack.append(char)
        elif char in CLOSING_SYMBOLS:
            try:
                prev_saved_symbol = stack.pop()
                if prev_saved_symbol != CLOSING_TO_OPENING_MAP[char]:
                    # every closing symbol should match opening symbol
                    return False
            except IndexError as e:
                # no previous symbols found
                # string is unbalances
                return False
        else:
            # just skip non braces, brackets, or parentheses
            continue
    # if all closing symbols were matched with opening symbols
    # stack should be empty
    return len(stack) == 0


class TestValidateBracetsNesting(
        unittest.TestCase):
    """
    Test validation for braces, brackets, and parentheses 
    nesting
    """

    def test_balanced_str(self):
        """
        Return true if string is perfectly balanced
        """
        str_ = '{[]()}()'
        self.assertTrue(
            are_braces_brackets_and_parentheses_balanced(str_))

    def test_balanced_str_with_gibberish_symbols(self):
        """
        We ignore non closing or opening symbols
        """
        str_ = '{aaa[bbb]ccc(ddd)   }'
        self.assertTrue(
            are_braces_brackets_and_parentheses_balanced(str_))

    def test_balanced_str_with_multiple_inner_layers(self):
        """
        Return true if string is perfectly balanced
        but has multiple inner layers
        """
        str_ = '{[({[()]})](((((((())))))))}'
        self.assertTrue(
            are_braces_brackets_and_parentheses_balanced(str_))

    def test_balanced_str_with_only_one_pair(self):
        """
        Return true if string is perfectly balanced
        but has only one pair of closing and opening symbols
        """
        str_ = '{}'
        self.assertTrue(
            are_braces_brackets_and_parentheses_balanced(str_))

    def test_inbalanced_str(self):
        """
        Return false if string is inbalanced
        """
        str_ = '{{]'
        self.assertFalse(
            are_braces_brackets_and_parentheses_balanced(str_))

    def test_inbalanced_str_starts_with_closing_symbol(self):
        """
        Return false if string is inbalanced and starts
        with closing symbol
        """
        str_ = ']{{}}()()()'
        self.assertFalse(
            are_braces_brackets_and_parentheses_balanced(str_))

    def test_inbalanced_str_with_only_opening_symbols(self):
        """
        Return false if string is inbalanced and has only opening symbols
        """
        str_ = '(({['
        self.assertFalse(
            are_braces_brackets_and_parentheses_balanced(str_))

    def test_inbalanced_str_with_multiple_layers(self):
        """
        Return false if string is inbalanced and has multiplr layers
        """
        str_ = '(({[{]}))'
        self.assertFalse(
            are_braces_brackets_and_parentheses_balanced(str_))


if __name__ == '__main__':
    unittest.main()