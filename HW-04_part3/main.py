# Створіть віртуальне оточення Python для ізоляції залежностей проекту.
# Скрипт має отримувати шлях до директорії як аргумент при запуску. 
# Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
# Використання бібліотеки colorama для реалізації кольорового виведення.
# Скрипт має коректно відображати як імена директорій, так і імена файлів, 
# використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).
# Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.

import sys
import os

from colorama import Fore, Style
from pathlib import Path

def list_directory_contents(dir_path, indent=0):
    try:
        dir_path = Path(dir_path)
        for entry in dir_path.iterdir():
            if entry.is_dir():
                print(Fore.BLUE + "  " * indent + entry.name + "/" + Style.RESET_ALL)
                list_directory_contents(entry, indent + 1)
            else:
                print(Fore.GREEN + "  " * indent + entry.name + Style.RESET_ALL)
    except FileNotFoundError:
        print("Директорію не знайдено.")
    except PermissionError:
        print("Відсутні права доступу до директорії.")

list_directory_contents("C:\Users\WORK\Desktop\GoIT\Repository\Python\HomeWork\goit-pycore-hw-04>")

