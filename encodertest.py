import unittest
from encoder import base64encoder


class TestEncodingMethods(unittest.TestCase):
    def test_encoding(self):
        s = "ABCDEFG"
        actual = "QUJDREVGRw=="
        self.assertEqual(base64encoder(s), actual)

if __name__ == '__main__':
    unittest.main()
