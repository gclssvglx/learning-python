import datetime
import unittest

from basics import Basics


class BasicsTestCase(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(Basics.say_hello("Fred"), "Hello Fred")

    def test_string_length(self):
        self.assertEqual(Basics.string_length("Hello World"), 11)

    def test_string_length_zero(self):
        self.assertEqual(Basics.string_length(""), 0)

    def test_print_quote(self):
        self.assertEqual(
            Basics.print_quote("These aren't the droids you're looking for", "Obi-Wan Kenobi"),
            "Obi-Wan Kenobi says, \"These aren't the droids you're looking for\""
        )

    def test_mad_lab(self):
        self.assertEqual(
            Basics.mad_lab("dog", "walk", "blue", "quickly"),
            "Do you walk your blue dog quickly? That's hilarious!"
        )

    def test_simple_math(self):
        self.assertEqual(
            Basics.simple_math(10, 5),
            ["10 + 5 = 15", "10 - 5 = 5", "10 * 5 = 50", "10 / 5 = 2"]
        )

    def test_retirement_calculator(self):
        current_date = datetime.datetime.now().year
        self.assertEqual(
            Basics.retirement_calculator(25, 65),
            "You have 40 years left. It's {}, so you can retire in {}.".format(current_date, current_date + 40)
        )


if __name__ == '__main__':
    unittest.main()
