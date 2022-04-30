from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
import random
import webbrowser
from tkinter import scrolledtext

randomsymbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
onePassLen = 1

window = Tk()
window.title("Password Generator by mrasdaf")
window.geometry("475x675")
window.config(bg="black")
window.resizable(width=False, height=False)



countOfPasswordsLabel = Label(window, text="Кол-во паролей:", bg="black", fg="white", font=("Comic Sans MS", 14))
countOfPasswordsLabel.place(x=30, y=50)

countOfPasswordsEntry = Entry(window, font=("Comic Sans MS", 14), bg="grey", fg="white")
countOfPasswordsEntry.place(x=200, y=50)

onePassLenEntry = Entry(window, font=("Comic Sans MS", 14), bg="grey", fg="white")
onePassLenEntry.place(x=200, y=100)

onePassLenLabel = Label(window, text="Кол-во символов в 1 пароле:", bg="black", fg="white", font="Arial 9")
onePassLenLabel.place(x=30, y=103)

def generateButtonClick():
    global randomsymbol
    global onePassLen
    cp = 0
    resultText.delete(1.0, "end")
    try:
        cp = int(countOfPasswordsEntry.get())
    except:
        resultText.insert(1.0, "Не удалось распознать число паролей!")
        return False
    try:
        onePassLen = int(onePassLenEntry.get())
    except:
        resultText.insert(1.0, "Не удалось распознать число символов в 1 пароле!")
        return False
    i = 1
    outputStr = ""
    res = ""
    outputStrFULL = ""
    while i <= cp:
        res = res + "\n"
        for u in range(onePassLen):
            res = res + random.choice(randomsymbols)
        outputStrFULL = outputStr + res + "\n"
        i += 1
        outputStr = ""
    resultText.insert(1.0, outputStrFULL)
    
def aboutButtonClick():
    messagebox.showinfo("О программе", """
Эта программа позволяет вам генерировать пароли.
Программа выбирает случайные символы из последовательности знаков и после чего выводит результат.
    
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
generateButton = Button(window, text="Сгенерировать", width=58, command=generateButtonClick, bg="grey", fg="white")
generateButton.place(x=31, y=150)

resultText = scrolledtext.ScrolledText(width=60, height=25, font=("Comic Sans MS", 9), bg="grey", fg="white")
resultText.place(x=25, y=200)

aboutButton = Button(window, text="О программе", width=15, command=aboutButtonClick, font=("Comic Sans MS", 9), bg="grey", fg="white")
aboutButton.place(x=350, y=643)

githublink = Button(window, text="Github", width=15, command=githubclick, font=("Comic Sans MS", 9), bg="grey", fg="white")
githublink.place(x=220, y=643)

githublink = Button(window, text="Сохранить результат", width=20, command=saveresult, font=("Comic Sans MS", 9), bg="grey", fg="white")
githublink.place(x=60, y=643)


window.mainloop()
