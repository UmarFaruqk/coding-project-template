import unittest

from translator import english_to_french, french_to_english

class TestTranslators(unittest.TestCase):
        def test_english_to_french(self):
            english_text = "Hello"
            expected_french_text = "Bonjour"
            translated_french_text = english_to_french(english_text)
            self.assertEqual(translated_french_text, expected_french_text)

        def test_french_to_english(self):
            french_text = "Bonjour"
            expected_english_text = "Hello"
            translated_english_text = french_to_english(french_text)
            self.assertEqual(translated_english_text, expected_english_text)

if __name__ == '__main__':
    unittest.main()        

