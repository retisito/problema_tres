import unittest

from get_list_of_infections import get_list_of_infections

# Tests adapted from `problem-specifications//canonical-data.json`


class TwoFerTest(unittest.TestCase):
    def test_no_name_given(self):
        self.assertEqual(get_list_of_infections(), "One for you, one for me.")

    def test_a_name_given(self):
        self.assertEqual(get_list_of_infections("Alice"), "One for Alice, one for me.")

    def test_another_name_given(self):
        self.assertEqual(get_list_of_infections("Bob"), "One for Bob, one for me.")


if __name__ == "__main__":
    unittest.main()
