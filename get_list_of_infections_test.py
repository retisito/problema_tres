import unittest

from get_list_of_infections import get_list_of_infections


class GetListOfInfectionsTest(unittest.TestCase):
    # Given a bad location json the output must be equal cero
    def test_output_bad_location_json_given(self):
        output, error = get_list_of_infections('ICD10Yjson')
        self.assertEqual(len(output), 0)

    # Given a bad location json the error must be "FileNotFoundError"
    def test_error_bad_location_json_given(self):
        output, error = get_list_of_infections('ICD10Yjson')    
        self.assertEqual(error.__class__.__name__, "FileNotFoundError")

    # Given a bad location json the output must be equal cero
    def test_output_bad_fomated_json_given(self):
        output, error = get_list_of_infections('ICD10X.json')        
        self.assertEqual(len(output), 0)

    # Given a bad location json the error must be "FileNotFoundError"
    def test_error_bad_fomated_json_given(self):
        output, error = get_list_of_infections('ICD10X.json')
        self.assertEqual(error.__class__.__name__, "JSONDecodeError")

    # Given a valid json the error must be "None"
    def test_error_valid_json_given(self):
        output, error = get_list_of_infections('ICD10.json')
        self.assertIsNone(error)

    # Given a valid json the output return values
    def test_output_valid_json_given(self):
        output, error = get_list_of_infections('ICD10.json')
        self.assertEqual(len(output), 304)

    # Given a valid json and a filter the output return values
    def test_output_and_filter_valid_json_given(self):
        output, error = get_list_of_infections('ICD10.json', ['salmonella'])
        self.assertEqual(len(output), 4)

        output, error = get_list_of_infections('ICD10.json', ['salmonella', 'escherichia coli'])
        self.assertEqual(len(output), 9)


if __name__ == "__main__":
    unittest.main()
