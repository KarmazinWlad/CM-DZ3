import unittest

from src.utils.errors import ConfigurationError
from src.utils.parser import parse_xml


class TestParser(unittest.TestCase):

    def test_parse_dict(self):
        data = {"key1": "value1", "key2": 123}
        expected = "begin\n key1 := \"value1\";\n key2 := 123;\nend"
        self.assertEqual(parse_xml(data), expected)

    def test_parse_array(self):
        data = {"array":["value1", 123], "key": "value"}
        expected = f"begin\n array := [ \"value1\", {123} ];\n key := \"value\";\nend"
        self.assertEqual(parse_xml(data), expected)


    def test_invalid_data_type(self):
        with self.assertRaises(ConfigurationError):
            parse_xml(None)

if __name__ == '__main__':
    unittest.main()
