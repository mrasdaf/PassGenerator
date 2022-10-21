# https://github.com/mrasdaf/PassGenerator
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
import random
import webbrowser
from tkinter import scrolledtext

import json
from os import path, getenv, mkdir


pp = getenv('APPDATA') + "\\PassGenerator\\"
if not path.isdir(getenv('APPDATA') + "\\PassGenerator"):
    mkdir(getenv('APPDATA') + "\\PassGenerator")
if not path.isfile(pp + "settings.json"):
    settings = {
        "theme": "dark"
    }
    with open(pp + "settings.json", "w") as f:
        json.dump(settings, f)
        f.close()

        
with open(pp + "settings.json", "r") as f:
    settings = json.load(f)
    


randomsymbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


window = Tk()
window.title("Password Generator by mrasdaf")
window.geometry("475x675")
window.config(bg="black")
window.resizable(width=False, height=False)

themec = StringVar()
themec.set("OFF")



countOfPasswordsLabel = Label(window, text="Кол-во паролей:", bg="black", fg="white", font=("Comic Sans MS", 14))
countOfPasswordsLabel.place(x=30, y=50)

countOfPasswordsEntry = Entry(window, font=("Comic Sans MS", 14), bg="#adadad", fg="white")
countOfPasswordsEntry.place(x=200, y=50)

onePassLenEntry = Entry(window, font=("Comic Sans MS", 14), bg="#adadad", fg="white")
onePassLenEntry.place(x=200, y=100)

onePassLenLabel = Label(window, text="Кол-во символов в 1 пароле:", bg="black", fg="white", font=("Comic Sans MS", 8))
onePassLenLabel.place(x=30, y=103)

def generateButtonClick():
    global randomsymbol # Делаем глобальными переменную с символами
    try:
        PasswordCount = int(countOfPasswordsEntry.get()) # Пробуем получить число паролей
    except:
        messagebox.showerror("Ошибка", "Введите корректное кол-во паролей!") # Ошибка
        return False
    try:
        onePassLen = int(onePassLenEntry.get()) # Получаем кол-во символов
    except:
        messagebox.showerror("Ошибка", "Введите корректное кол-во символов в одном пароле!") # Ошибка
        return False
    if PasswordCount <= 0:
        messagebox.showerror("Ошибка", "Введите положительное целое число!")
        return False
    if onePassLen <= 0:
        messagebox.showerror("Ошибка", "Введите положительное целое число!")
        return False
    savebutton.config(state=DISABLED)
    resultText.config(state=NORMAL)
    resultText.delete(1.0, "end") # Очищаем вывод
    resultText.config(state=DISABLED)
    i = 1 # Определяем счетчик
    res = "" # Создаем пустой результат
    while i <= PasswordCount: # Пока не создадим 1 пароль
        for u in range(onePassLen): # Пока не сгенерируем нужное количество символов
            res = res + random.choice(randomsymbols) # Генерация строки с 1 паролем
        res = res + "\n" # Добавление переноса строки
        i += 1
    resultText.config(state=NORMAL)
    resultText.insert(1.0, res) # Вставка в вывод
    resultText.config(state=DISABLED)
    savebutton.config(state=NORMAL)
    
def aboutButtonClick():
    messagebox.showinfo("О программе", """Эта программа позволяет вам генерировать пароли.
Программа выбирает случайные символы из последовательности знаков и после чего выводит результат.
    
Настройки приложения находятся в %appdata%/settings.json

by mrasdaf
Написано на Python
    """)
    
def githubclick():
    webbrowser.open_new_tab('https:\\github.com\mrasdaf\PassGenerator')
def saveresult():
    try:
        Files = (
                ("Текстовые файлы блокнота", "*.txt"),
                ("Все файлы", "*.*")
                )
        filename = fd.asksaveasfilename(
            filetypes = Files,
            defaultextension = Files
            )
        with open(filename, "w") as f:
            s = resultText.get(1.0, END)
            f.write(s)
            f.close()
    except:
        return False
def switchtheme():
    if themec.get() == "ON":
        # Включаем светлую тему
        window.config(bg = "white")
        generateButton.config(bg = "white", fg="black")
        aboutButton.config(bg = "white", fg="black")
        githublink.config(bg = "white", fg="black")
        savebutton.config(bg = "white", fg="black")
        countOfPasswordsLabel.config(bg = "white", fg="black")
        countOfPasswordsEntry.config(bg = "white", fg="black")
        onePassLenLabel.config(bg = "white", fg="black")
        onePassLenEntry.config(bg = "white", fg="black")
        resultText.config(bg = "white", fg="black")
        settings["theme"] = "light"
        with open(pp + "settings.json", "w") as f:
            json.dump(settings, f)            
    if themec.get() == "OFF":
        # Выключаем светлую тему
        window.config(bg = "black")
        generateButton.config(bg = "#adadad", fg="white")
        aboutButton.config(bg = "#adadad", fg="white")
        githublink.config(bg = "#adadad", fg="white")
        savebutton.config(bg = "#adadad", fg="white")
        countOfPasswordsLabel.config(bg = "black", fg="white")
        countOfPasswordsEntry.config(bg = "#adadad", fg="white")
        onePassLenLabel.config(bg = "black", fg="white")
        onePassLenEntry.config(bg = "#adadad", fg="white")
        resultText.config(bg = "#adadad", fg="white")
        settings["theme"] = "dark"
        with open(pp + "settings.json", "w") as f:
            json.dump(settings, f)  

generateButton = Button(window, text="Сгенерировать", width=58, command=generateButtonClick, bg="#adadad", fg="white")
generateButton.place(x=31, y=150)

resultText = scrolledtext.ScrolledText(width=60, height=25, font=("Comic Sans MS", 9), bg="#adadad", fg="white")
resultText.place(x=25, y=200)
resultText.config(state=DISABLED)

aboutButton = Button(window, text="О программе", width=15, command=aboutButtonClick, font=("Comic Sans MS", 9), bg="#adadad", fg="white")
aboutButton.place(x=350, y=643)

githublink = Button(window, text="Github", width=15, command=githubclick, font=("Comic Sans MS", 9), bg="#adadad", fg="white")
githublink.place(x=220, y=643)

savebutton = Button(window, text="Сохранить результат", width=20, command=saveresult, font=("Comic Sans MS", 9), bg="#adadad", fg="white")
savebutton.place(x=60, y=643)
savebutton.config(state=DISABLED)

selecttheme = Checkbutton(window, text="Светлая тема", command=switchtheme, width=20, font=("Comic Sans MS", 9), bg="#adadad", fg="black", variable=themec, onvalue="ON", offvalue="OFF")
selecttheme.place(x=300, y=10)
# print(settings)
if settings["theme"] == 'light':
    selecttheme.select()
    switchtheme()
    
window.mainloop()
