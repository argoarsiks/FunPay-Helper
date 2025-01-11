import pyperclip
import keyboard
from core import translate
import pyautogui as pg
import config


def translator():
    text = pyperclip.paste()
    result_text = translate(text)
    pyperclip.copy(result_text)
    pg.hotkey('ctrl', 'v')


def main():
    print("""
███████╗██╗░░░██╗███╗░░██╗██████╗░░█████╗░██╗░░░██╗██╗░░██╗███████╗██╗░░░░░██████╗░███████╗██████╗░
██╔════╝██║░░░██║████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝██║░░██║██╔════╝██║░░░░░██╔══██╗██╔════╝██╔══██╗
█████╗░░██║░░░██║██╔██╗██║██████╔╝███████║░╚████╔╝░███████║█████╗░░██║░░░░░██████╔╝█████╗░░██████╔╝
██╔══╝░░██║░░░██║██║╚████║██╔═══╝░██╔══██║░░╚██╔╝░░██╔══██║██╔══╝░░██║░░░░░██╔═══╝░██╔══╝░░██╔══██╗
██║░░░░░╚██████╔╝██║░╚███║██║░░░░░██║░░██║░░░██║░░░██║░░██║███████╗███████╗██║░░░░░███████╗██║░░██║
╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
          \n\n""")
    if config.launguage not in ['en', 'ru']:
        print('Select language: en or ru:')
        language = input().strip()
        with open("config.py", "w", encoding="utf-8") as config_file:
            config_file.write(f"launguage = '{language}'\n")
    elif config.launguage == 'ru':      
        print(f'Список команд:\n'
            f'F2: Перевод текста\n'
            f'ESC: Выход')
    elif config.launguage == 'en':
        print(f'Command list:\n'
            f'F2: Translate text\n'
            f'ESC: Exit')
    keyboard.add_hotkey('F2', translator)
    keyboard.wait('esc')                


if __name__ == '__main__':
    main()