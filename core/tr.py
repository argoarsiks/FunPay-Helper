from translate import Translator
from langdetect import detect

def translate(pasted_text):
    from_lang = detect(pasted_text)
    if from_lang == 'en':
        to_lang = 'ru'
    elif from_lang == 'mk' or from_lang == 'ru':
        to_lang = 'en'
    translator = Translator(from_lang=from_lang, to_lang=to_lang)
    copy_text = translator.translate(pasted_text)
    return copy_text
