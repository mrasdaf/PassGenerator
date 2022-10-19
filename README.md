# PassGenerator
Генератор паролей (от mrasdaf)

Эта программа позволяет вам создавать сложные сгенерированные пароли.

Написано на python с использованием tkinter

![изображение](https://user-images.githubusercontent.com/104437646/166146390-452c476b-83ae-48a7-9aeb-d7e21acc7d88.png)

# Системные требования
1. При запуске из .py файла

   * ОС: Любая *(тестировалось на Windows)*

   * Python 3.7+

   * Для сборки EXE требуется модуль *pyinstaller*

2. При запуске из EXE файла

   * ОС: Windows 10

   * Установка Python не требуется

# Сборка
1. Установить модуль *pyinstaller*, если он еще не установлен:

   `pip install pyinstaller`

2. Собрать приложение:

   `pyinstaller -F -w -i icon.ico main.py`

Полученный файл будет лежать в папке **dist**
