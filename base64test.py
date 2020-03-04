import unittest
from encoder import base64encoder
from decoder import base64decoder


class TestEncodingMethods(unittest.TestCase):
    def test_encoding(self):
        s = "ABCDEFG"
        actual = "QUJDREVGRw=="
        self.assertEqual(base64encoder(s), actual)


    def test_decoding(self):
        s = "QUJDREVGRw=="
        actual = "ABCDEFG"
        self.assertEqual(base64decoder(s), actual)


    def test_encdec(self):
        s = "omgasgadssgajk"
        e = base64encoder(s)
        self.assertEqual(base64decoder(e), s)

if __name__ == '__main__':
    unittest.main()
