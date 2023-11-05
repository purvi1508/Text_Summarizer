from googletrans import Translator

def translate_to_english(text):
    try:
        translator = Translator()
        translated = translator.translate(text, dest="en")
        return translated.text
    except Exception as e:
        print(f"Translation to English failed: {e}")
        return text  # Return the original text on failure

def translate_to_hindi(text):
    try:
        translator = Translator()
        translated = translator.translate(text, dest="hi")
        return translated.text
    except Exception as e:
        print(f"Translation to Hindi failed: {e}")
        return text  # Return the original text on failure

def translate_to_japanese(text):
    try:
        translator = Translator()
        translated = translator.translate(text, dest="ja")
        return translated.text
    except Exception as e:
        print(f"Translation to Japanese failed: {e}")
        return text  # Return the original text on failure

def translate_to_korean(text):
    try:
        translator = Translator()
        translated = translator.translate(text, dest="ko")
        return translated.text
    except Exception as e:
        print(f"Translation to Korean failed: {e}")
        return text  # Return the original text on failure
