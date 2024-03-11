import unittest
from unittest.mock import patch
from io import StringIO

from logic_circuit import format_input


class TestFormatInput(unittest.TestCase):
    @patch('builtins.input', return_value='9')
    def test_proper_number(self, mock_input):
        result = format_input()
        self.assertEqual(result, '0b1001')

    @patch('builtins.input', side_effect=['gfb','23','3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_input_out_of_bounds_number(self, mock_stdout, mock_input):
        result = format_input()
        self.assertIn(
            "Input type must be int",
            mock_stdout.getvalue()        
        )
        self.assertIn(
            "Input must be an integer between [0,9]", 
            mock_stdout.getvalue()
        )
        self.assertEqual(result, '0b0011')


if __name__ == '__main__':
    unittest.main()
