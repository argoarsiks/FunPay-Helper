import pyperclip
import keyboard
from translate import Translator
import time
import pyautogui
from config import autopress_enter, language

if language == 'ru':
    print(f'Выберите действие:\n'
    f'1: Запуск на F2, для автопервода')
elif language == 'en':
    print(f'Select an action:\n'
    f'1: Start on F2, for auto drive')

while True:
    translator = Translator(from_lang='ru', to_lang='en')
    if keyboard.is_pressed('F2'):
        pasted_text = pyperclip.paste()
        text_parts = [pasted_text[i:i + 500] for i in range(0, len(pasted_text), 500)]
        for idx, part in enumerate(text_parts, start=1):
            translated_part = translator.translate(part)
            copy_text = pyperclip.copy(translated_part)
            pyautogui.hotkey('ctrl', 'v')
        if autopress_enter == True:
            pyautogui.press('enter')
        time.sleep(0.1)
