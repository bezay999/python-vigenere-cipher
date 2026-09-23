import unittest

from vigenere import decrypt, encrypt


class VigenereTest(unittest.TestCase):
    def test_encrypts_known_example(self):
        self.assertEqual("Lxfopv ef Rnhr!", encrypt("Attack at Dawn!", "LEMON"))

    def test_decrypts_known_example(self):
        self.assertEqual("Attack at Dawn!", decrypt("Lxfopv ef Rnhr!", "LEMON"))

    def test_preserves_numbers_and_punctuation(self):
        self.assertEqual("Bcd 123!", encrypt("Abc 123!", "B"))

    def test_rejects_empty_key(self):
        with self.assertRaises(ValueError):
            encrypt("Hello", "")

    def test_rejects_non_letter_key(self):
        with self.assertRaises(ValueError):
            encrypt("Hello", "key-123")


if __name__ == "__main__":
    unittest.main()

