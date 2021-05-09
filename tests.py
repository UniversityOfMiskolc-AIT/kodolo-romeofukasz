import unittest
from kodolo import encode, decode, string_is_integer


class EncodeTestCase(unittest.TestCase):

    def test_encode_alma(self):
        self.assertEqual(encode("alma"), "97, 11, 1, -12")

    def test_encode_almakukac(self):
        self.assertEqual(encode("Alma@"), "65, 43, 1, -12, -33")

    def test_if_non_ascii_input_raises_value_error(self):
        with self.assertRaises(ValueError):
            encode("almáspite")

    def test_if_non_string_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            encode(15.0)


class StringIsIntegerTestCase(unittest.TestCase):

    def test_if_non_string_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            string_is_integer(555)

    def test_string_is_integer_123(self):
        self.assertTrue(string_is_integer("123"))

    def test_string_is_integer_plus_123(self):
        self.assertTrue(string_is_integer("+123"))

    def test_string_is_integer_minus_123(self):
        self.assertTrue(string_is_integer("-123"))

    def test_string_is_integer_alma(self):
        self.assertFalse(string_is_integer("alma"))


class DecodeTestCase(unittest.TestCase):

    def test_decode_alma(self):
        self.assertEqual(decode("97, 11,  1, -12"), "alma")

    def test_decode_almakukac(self):
        self.assertEqual(decode("65, 43, 1, -12, -33"), "Alma@")

    def test_if_non_ascii_codes_raises_value_error(self):
        with self.assertRaises(ValueError):
            decode("97, 11, 1, 116, -110, -3, -7, 11, -15")  # almáspite

    def test_if_invalid_input_raises_value_error(self):
        with self.assertRaises(ValueError):
            decode("65, 1000, -42")

    def test_if_non_string_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            decode(True)


if __name__ == "__main__":
    unittest.main()
