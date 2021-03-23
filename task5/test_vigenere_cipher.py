""" module which test vigenere_cipher module """
from unittest import TestCase
from unittest import main as unittest_run
from vigenere_cipher import (
    VigenereCipher,
    combine_character,
    separate_character,
)


class TestPoint(TestCase):
    """ class TestPoint """
    def setUp(self) -> None:
        """ create values for testing """
        self.cipher = VigenereCipher("TRAIN")

    def test_encode(self):
        """ test encoding """
        encoded = self.cipher.encode("ENCODEDINPYTHON")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")

    def test_encode_character(self):
        """ test encoding one character """
        encoded = self.cipher.encode("E")
        self.assertEqual(encoded, "X")

    def test_encode_spaces(self):
        """ test encoding text with spaces """
        encoded = self.cipher.encode("ENCODED IN PYTHON")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")

    def test_encode_lowercase(self):
        """ test encoding text with lowercase """
        encoded = self.cipher.encode("encoded in Python")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")

    def test_combine_character(self):
        """ test combine_character function """
        self.assertEqual(combine_character("E", "T"), "X")
        self.assertEqual(combine_character("N", "R"), "E")

    def test_extend_keyword(self):
        """ test extend_keyword method """
        extended = self.cipher.extend_keyword(16)
        self.assertEqual(extended, "TRAINTRAINTRAINT")
        extended = self.cipher.extend_keyword(15)
        self.assertEqual(extended, "TRAINTRAINTRAIN")

    def test_separate_character(self):
        """ test separate_character function """
        self.assertEqual(separate_character("X", "T"), "E")
        self.assertEqual(separate_character("E", "R"), "N")

    def test_decode(self):
        """ test decoding """
        decoded = self.cipher.decode("XECWQXUIVCRKHWA")
        self.assertEqual(decoded, "ENCODEDINPYTHON")


if __name__ == '__main__':
    unittest_run()
