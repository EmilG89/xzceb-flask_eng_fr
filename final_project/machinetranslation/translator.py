'''This module uses python3 deep_translator to translete english to french and french to english.'''

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''This function takes english text and return it in french.'''
    text = english_text

    french_text= MyMemoryTranslator(source='english',target='french').translate(text)

    return french_text

def french_to_english(french_text):
    '''This function takes french text and return it in english.'''
    text = french_text

    english_text = MyMemoryTranslator(source='french', target='english').translate(text)

    return english_text
