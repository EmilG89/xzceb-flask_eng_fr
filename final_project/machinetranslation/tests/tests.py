'''This module test translator.py functions.'''

import unittest
import sys
sys.path.append('..')

from machinetranslation import translator

class E2FTranslationTestCase(unittest.TestCase):
    def test_translation_e2f(self):
        text = "Hello"
        translation = translator.english_to_french(text)
        self.assertEqual(translation, "Bonjour")
        self.assertNotEqual(translation, " ")

class F2ETranslationTestCase(unittest.TestCase):
    def test_translation_f2e(self):
        text = "Bonjour"
        translation = translator.french_to_english(text)
        self.assertEqual(translation, "Hello")
        self.assertNotEqual(translation, " ")
      
unittest.main()
