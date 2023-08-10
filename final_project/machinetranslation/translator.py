"""
A module for translating languages
"""
from deep_translator import MyMemoryTranslator
def english_to_french(english_text):
    """ translating engish text to french """
    french_to_english_translate = MyMemoryTranslator(
        source='english', target = 'french').translate(english_text)
    return french_to_english_translate

def french_to_english(french_text):
    """translating frrench text to english """
    english_to_french_translate = MyMemoryTranslator(
        source='french', target='english').translate(french_text)
    return english_to_french_translate    