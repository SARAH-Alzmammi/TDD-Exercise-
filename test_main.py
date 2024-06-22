import pytest

from main import Calculator


class TestCalculator:
    calculator = Calculator()

    def test_adding_one_number(self):
        assert self.calculator.add('5') == 5, "Add one number successfully"

    def test_passing_empty_string(self):
        assert self.calculator.add('') == 0, "Add Zero number successfully"

    def test_adding_two_numbers_successfully(self):
        assert self.calculator.add('5,6') == 11, "Add two numbers successfully"

    def test_adding_three_numbers_successfully(self):
        assert self.calculator.add('5,6,7') == 18, "Add three numbers successfully"

    def test_adding_three_numbers_with_new_line_delimiters(self):
        assert self.calculator.add('3\n3\n3') == 9, "Add three numbers with new line delimiters successfully"

    def test_adding_four_numbers_with_mix_delimiters(self):
        assert self.calculator.add('3,3,3\n5') == 14, "Add four numbers with mix delimiters successfully"

    def test_failing_with_a_delimiter_at_the_end(self):
        with pytest.raises(Exception):
            self.calculator.add('3,3,')

    def test_success_with_a_delimiter_change(self):
        assert self.calculator.add('//sep\n2sep5') == 7, "Change delimiter successfully"

    def test_failing_with_a_delimiter_change(self):
        with pytest.raises(Exception):
            self.calculator.add('//|\n1|2,3')
