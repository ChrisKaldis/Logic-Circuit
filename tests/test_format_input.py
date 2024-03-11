import unittest
from unittest.mock import patch

from logic_circuit import format_input


class TestFormatInput(unittest.TestCase):

    @patch('builtins.input', return_value = '7')
    def test_format_input_in_bounds_number(self, mock_input):
        self.assertEqual(format_input(), '0111')


if __name__ == '__main__':
    unittest.main()
