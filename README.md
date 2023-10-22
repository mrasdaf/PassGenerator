Ссылка на оригинальную иконку: https://www.pinclipart.com/maxpin/iRJTRx/

# PassGenerator
Генератор паролей (от mrasdaf)

Эта программа позволяет вам создавать сложные сгенерированные пароли.

Написано на python с использованием tkinter

![PassGenerator_v1 1 2_pEeJmI85e7](https://user-images.githubusercontent.com/104437646/197220979-12a62bfb-5c47-40e5-943a-3e03b25e112c.png)

# Системные требования
1. При запуске из .py файла

   * ОС: Windows

   * Python 3.7+

   * Для сборки EXE требуется модуль *pyinstaller*

2. При запуске из EXE файла

   * ОС: В зависимости от ОС, на которой была собрано приложение

   * Установка Python не требуется

# Сборка
1. Установить модуль *pyinstaller*, если он еще не установлен:

   `pip install pyinstaller`

2. Собрать приложение:

   `pyinstaller -F -w -i icon.ico main.py`

Полученный файл будет лежать в папке **dist**



